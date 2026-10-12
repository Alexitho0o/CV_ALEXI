"""Soporte reproducible de activos y comprobaciones. No es un ATS comercial."""
from __future__ import annotations
import base64, io, json, mimetypes, re, shutil, subprocess, unicodedata
from pathlib import Path
from urllib.parse import unquote, urlparse
from PIL import Image
import fitz
from pypdf import PdfReader


def read_data(project: Path) -> dict:
    code = "import * as data from './src/data.js'; console.log(JSON.stringify(data));"
    return json.loads(subprocess.check_output(['node','--input-type=module','-e',code],cwd=project,text=True))


def expected_phrases(data: dict) -> list[str]:
    values=[data['profile']['name'][0],data['profile']['name'][1],data['profile']['title'],data['profile']['summary']]
    values += [data['profile'][k] for k in ('phone','email','linkedin')]
    for f in data['quickFacts']:
        values.extend([v for v in (f['label'],f.get('sub')) if v])
    for a in data['areas']: values.extend([a['title'],*a['bullets']])
    for k in data['kpis']: values.extend([k['number'],k['title'],k['text']])
    for h in data['trayectoria']:
        values.extend([h[k] for k in ('role','period','institution','sub','desc')])
    for e in data['education']: values.extend([e[k] for k in ('title','institution','detail')])
    for g in data['toolGroups']: values.extend([g['label'],*g['items']])
    for v in data['valueProps']: values.extend([v['title'],v['text']])
    values.extend(data['interests'])
    for m in data['impactModel']: values.extend([m['title'],m['sub']])
    values.append(data['quote'])
    return list(dict.fromkeys(values))


def normalized(text: str) -> str:
    return re.sub(r'\s+',' ',unicodedata.normalize('NFC',text).replace('\u00ad','')).strip().casefold()


def image_bytes(path: Path) -> tuple[bytes,str]:
    """Optimiza solo copias de impresión; mantiene el original y el QR sin pérdidas."""
    raw=path.read_bytes(); mime=mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
    if path.name == 'CONTACTO.png' or len(raw) < 150_000:
        return raw,mime
    with Image.open(path) as image:
        image.thumbnail((1200,1200),Image.Resampling.LANCZOS)
        opaque='A' not in image.getbands() or image.getchannel('A').getextrema()==(255,255)
        out=io.BytesIO()
        if opaque:
            image.convert('RGB').save(out,format='JPEG',quality=92,optimize=True)
            return out.getvalue(),'image/jpeg'
        image.save(out,format='PNG',optimize=True)
        return out.getvalue(),'image/png'


def inline_build(project: Path,view: str='visual') -> str:
    """Render offline del mismo bundle de Vite, sin cambiar componentes ni estilos."""
    dist=project/'dist'; html=(dist/'index.html').read_text(encoding='utf-8')
    for src in re.findall(r'<link[^>]*href="(/assets/[^\"]+\.css)"[^>]*>',html):
        css=(dist/src.lstrip('/')).read_text(encoding='utf-8')
        html=re.sub(r'<link[^>]*href="'+re.escape(src)+r'"[^>]*>',lambda m:'<style>'+css+'</style>',html)
    for src in re.findall(r'<script[^>]*src="(/assets/[^\"]+\.js)"[^>]*></script>',html):
        js=(dist/src.lstrip('/')).read_text(encoding='utf-8')
        for path in (dist/'img').iterdir():
            if path.is_file() and path.suffix.lower() in ('.png','.jpg','.jpeg') and '/img/'+path.name in js:
                content,mime=image_bytes(path)
                js=js.replace('/img/'+path.name,'data:'+mime+';base64,'+base64.b64encode(content).decode())
        html=re.sub(r'<script[^>]*src="'+re.escape(src)+r'"[^>]*></script>',lambda m:'<script>window.__CV_OUTPUT_VIEW__='+json.dumps(view)+';</script><script type="module">'+js+'</script>',html)
    return html


def attach_image_routes(page,project: Path):
    root=(project/'public/img').resolve()
    def handler(route):
        url=urlparse(route.request.url); tail=unquote(url.path).partition('/img/')[2]
        path=(root/tail).resolve()
        if path.is_relative_to(root) and path.is_file() and path.suffix.lower() in ('.png','.jpg','.jpeg'):
            raw,mime=image_bytes(path);route.fulfill(status=200,content_type=mime,body=raw)
        else:route.continue_()
    page.route('**/img/**',handler)


def decode_qr(image: Image.Image) -> str:
    try:
        import zxingcpp
        found=zxingcpp.read_barcode(image)
        return found.text if found else ''
    except ImportError:
        from pyzbar.pyzbar import decode
        codes=decode(image)
        return codes[0].data.decode('utf-8') if codes else ''


def verify_pdf(pdf: Path,data: dict,visual: bool=True) -> dict:
    """Contrasta todas las frases con dos motores y, cuando existe, Poppler."""
    doc=fitz.open(pdf);reader=PdfReader(pdf)
    texts={'pymupdf':'\n'.join(p.get_text() for p in doc),'pypdf':'\n'.join(p.extract_text() or '' for p in reader.pages)}
    if shutil.which('pdftotext'):
        texts['poppler']=subprocess.check_output(['pdftotext','-enc','UTF-8',str(pdf),'-'],text=True)
    phrases=expected_phrases(data); missing={}
    for engine,text in texts.items():
        norm=normalized(text);missing[engine]=[phrase for phrase in phrases if normalized(phrase) not in norm]
    fonts=[font for p in doc for font in p.get_fonts()]
    badchars={engine:sorted({ch for ch in text if ch=='\ufffd' or ch=='\x00' or 0xE000<=ord(ch)<=0xF8FF}) for engine,text in texts.items()}
    fulltext=texts['pymupdf']
    tool_items=[t for g in data['toolGroups'] for t in g['items']]
    ordered_roles=[normalized(h['role']) for h in data['trayectoria']]
    norm=normalized(fulltext);start=norm.find('trayectoria profesional'); positions=[]
    for role in ordered_roles:
        found=norm.find(role,start);positions.append(found);start=found+len(role) if found>=0 else start
    measured=[s['size'] for p in doc for b in p.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans'] if s['text'].strip()]
    result={'pages':len(doc),'a4':all(abs(p.rect.width-595.276)<1 and abs(p.rect.height-841.89)<1 for p in doc),'bytes':pdf.stat().st_size,'encrypted':bool(reader.is_encrypted),'tagged':'/StructTreeRoot' in reader.trailer['/Root'],'phrases_checked':len(phrases),'missing_phrases':missing,'invalid_characters':badchars,'tools_expected':len(tool_items),'tools_found':sum(normalized(t) in norm for t in tool_items),'experiences_expected':len(ordered_roles),'experiences_in_order':all(x>=0 for x in positions) and positions==sorted(positions),'min_font_pt':round(min(measured),2),'max_font_pt':round(max(measured),2),'type3_fonts':any(f[2]=='Type3' for f in fonts),'font_programs_embedded':all(bool(doc.extract_font(f[0])[3]) for f in fonts)}
    if visual:
        page=doc[0];code=''
        for item in page.get_image_info(xrefs=True):
            xref=item['xref']
            if not xref:continue
            content=doc.extract_image(xref)
            im=Image.open(io.BytesIO(content['image']))
            if im.width==650 and im.height==650:
                code=decode_qr(im);bbox=fitz.Rect(item['bbox']);pix=page.get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=bbox)
                rendered=decode_qr(Image.open(io.BytesIO(pix.tobytes('png'))))
                result['qr_decoded_at_300dpi']=bool(code) and code==rendered
                result['qr_square']=abs(bbox.width-bbox.height)<.1
                result['qr_size_mm']=round(bbox.width*25.4/72,2)
                break
        correct='https://'+data['profile']['linkedin'].replace('linkedin.com','www.linkedin.com',1)
        result['qr_correct_linkedin']=('URL:'+correct in code and '%253A' not in code)
        result['qr_contains_contacts']=data['profile']['email'] in code and data['profile']['phone'] in code
    errors=[]
    if visual and result['pages']!=1:errors.append('El CV visual debe tener exactamente una página.')
    if not result['a4']:errors.append('Formato distinto de A4.')
    if result['encrypted']:errors.append('PDF cifrado.')
    if any(missing.values()):errors.append('Hay texto fuente no recuperado por algún motor.')
    if any(badchars.values()):errors.append('Caracteres no válidos en la extracción.')
    if not result['experiences_in_order']:errors.append('Orden de las experiencias incoherente.')
    if not result['font_programs_embedded'] or result['type3_fonts']:errors.append('Fuentes no aptas para el control de extracción.')
    if result['bytes']>=2_500_000:errors.append('PDF mayor al umbral de 2,5 MB utilizado en esta auditoría.')
    if visual and not all(result.get(k,False) for k in ('qr_decoded_at_300dpi','qr_square','qr_correct_linkedin','qr_contains_contacts')):errors.append('Falló la validación del QR.')
    for engine,text in texts.items():pdf.with_name(pdf.stem+'_'+engine+'.txt').write_text(text,encoding='utf-8')
    result['errors']=errors;doc.close();return result
