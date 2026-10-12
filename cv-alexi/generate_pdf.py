#!/usr/bin/env python3
"""CV gobernado: Vite -> Chromium -> validación -> publicación atómica.

Uso:
  python3 generate_pdf.py --preview --with-ats --desktop
  python3 generate_pdf.py --offline --with-ats

Se conserva la escala CSS 0.709; Playwright siempre imprime con scale=1.
No modifica src, los originales de imágenes ni el historial de Git.
"""
from __future__ import annotations
import argparse, datetime, hashlib, json, os, shutil, socket, subprocess, sys, time
from pathlib import Path

PROJECT=Path(__file__).resolve().parent
try:
    from playwright.sync_api import sync_playwright
    from scripts.pdf_support import read_data,inline_build,attach_image_routes,verify_pdf
except ImportError as exc:
    venv=Path.home()/'venv/bin/python3'
    if venv.is_file() and Path(sys.executable).resolve()!=venv.resolve():
        os.execv(str(venv),[str(venv),*sys.argv])
    raise SystemExit(f'Falta una dependencia: {exc}. Ejecuta: python3 -m pip install -r requirements-pdf.txt')

DEFAULT_SCALE=0.709
OUTPUT_NAME='CV_Alexi_Marcelo_Burgos_Flores_visual.pdf'
ATS_NAME='CV_Alexi_Marcelo_Burgos_Flores_LECTURA_ATS.pdf'


def args():
    p=argparse.ArgumentParser(description='Generar CV A4 con validación de contenido y QR.')
    p.add_argument('--preview',action='store_true',help='Build limpio + preview (modo predeterminado).')
    p.add_argument('--offline',action='store_true',help='Build y render del mismo bundle sin red ni servidor.')
    p.add_argument('--with-ats',action='store_true',help='Añadir PDF de lectura lineal con TODO el contenido.')
    p.add_argument('--desktop',action='store_true',help='Copiar los PDF validados a ~/Desktop.')
    p.add_argument('--scale',type=float,default=DEFAULT_SCALE)
    p.add_argument('--out',default=OUTPUT_NAME,help='Nombre del CV visual; sin rutas.')
    p.add_argument('--no-open',action='store_true',help='No abrir el visor al terminar.')
    p.add_argument('--port',type=int,default=4173)
    return p.parse_args()


def atomic_copy(src: Path,dst: Path):
    if src.resolve()==dst.resolve():return
    temp=dst.with_name('.'+dst.name+'.tmp')
    shutil.copy2(src,temp);os.replace(temp,dst)


def layout_check(page,visual: bool) -> dict:
    r=page.evaluate('''() => {
      const cv=document.querySelector('.cv-page'),r=cv.getBoundingClientRect();
      const selectors=['.cv-hero','.cv-kpi','.cv-footer','.qr-img','.photo'];
      const fields=['.hero-title','.hero-summary','.hito-role','.hito-inst','.hito-sub','.hito-desc','.tool-tag','.edu-title','.val-text','.kpi-text'];
      return {width:r.width,height:r.height,sections:Object.fromEntries(selectors.map(s=>[s,!!document.querySelector(s)])),
        images:document.images.length,failedImages:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).length,
        fallbacks:document.querySelectorAll('.img-fallback').length,
        horizontalOverflow:document.documentElement.scrollWidth>document.documentElement.clientWidth+2,
        fieldSizes:Object.fromEntries(fields.map(s=>{let e=document.querySelector(s);return [s,e?parseFloat(getComputedStyle(e).fontSize):null]}))};
    }''')
    if visual:
        if not all(r['sections'].values()):raise RuntimeError('Falta una sección del CV visual.')
        if r['width']>794 or r['height']>1122:raise RuntimeError(f'El layout excede A4: {r["width"]:.2f} x {r["height"]:.2f} px.')
        if r['failedImages'] or r['fallbacks'] or r['horizontalOverflow']:raise RuntimeError('Fallo de imágenes u overflow horizontal.')
    return r


def generate(browser,project: Path,data: dict,output: Path,options,view: str,url: str|None):
    visual=view=='visual'
    page=browser.new_page(viewport={'width':1200,'height':1800},device_scale_factor=1)
    errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    attach_image_routes(page,project)
    try:
        if options.offline:
            page.set_content(inline_build(project,view),wait_until='networkidle',timeout=45000)
        else:
            page.goto(url+('?view=ats' if not visual else ''),wait_until='networkidle',timeout=45000)
        page.wait_for_selector('.cv-page',state='visible',timeout=15000)
        page.evaluate('(scale)=>document.documentElement.style.setProperty("--print-scale",String(scale))',options.scale)
        page.emulate_media(media='print')
        page.evaluate('''async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));}''')
        if errors:raise RuntimeError('Errores de React: '+'; '.join(errors))
        layout=layout_check(page,visual)
        expected_path=output.with_name('.'+output.name+'.candidate.pdf')
        page.pdf(path=str(expected_path),format='A4',print_background=True,prefer_css_page_size=True,
                 margin={'top':'0','right':'0','bottom':'0','left':'0'},scale=1.0,tagged=True,outline=True)
        checks=verify_pdf(expected_path,data,visual)
        if checks['errors']:
            output.with_suffix('.validation.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
            raise RuntimeError(' / '.join(checks['errors']))
        os.replace(expected_path,output)
        for engine in checks['missing_phrases']:
            old=expected_path.with_name(expected_path.stem+'_'+engine+'.txt')
            os.replace(old,output.with_name(output.stem+'_'+engine+'.txt'))
        checks['sha256']=hashlib.sha256(output.read_bytes()).hexdigest()
        return {'file':output.name,'view':view,'layout':layout,'checks':checks}
    finally:page.close()


def report(results: list,options,error: str|None=None):
    lines=['# PDF_GENERATION_REPORT','',f'Generado: {datetime.datetime.now(datetime.timezone.utc).isoformat()}',
           f'Método: Vite build + Chromium ({"bundle offline" if options.offline else "preview"}).',
           f'Escala CSS visual: {options.scale}; escala Playwright: 1.0.','',
           'No se han ejecutado pruebas en un ATS comercial ni realizado una postulación. La extracción local no garantiza selección ni parsing idéntico en todos los ATS.','']
    if error:lines+=['## ERROR',error,'No se copió ningún PDF al Escritorio.','']
    for item in results:
        c=item['checks']; l=item['layout']
        lines += [f'## {item["file"]}',f'- SHA-256: `{c["sha256"]}`',f'- Páginas: {c["pages"]}; A4: {c["a4"]}; bytes: {c["bytes"]}.',
                  f'- Texto etiquetado: {c["tagged"]}; cifrado: {c["encrypted"]}; fuentes incrustadas: {c["font_programs_embedded"]}; fuentes Type3: {c["type3_fonts"]}.',
                  f'- Frases contrastadas por motor: {c["phrases_checked"]}; faltantes: {json.dumps(c["missing_phrases"],ensure_ascii=False)}.',
                  f'- Herramientas recuperadas: {c["tools_found"]}/{c["tools_expected"]}; experiencias ordenadas: {c["experiences_in_order"]}.',
                  f'- Caracteres inválidos: {json.dumps(c["invalid_characters"],ensure_ascii=False)}.',
                  f'- Layout: {l["width"]:.2f} × {l["height"]:.2f} px; imágenes: {l["images"]}; errores de imagen: {l["failedImages"]}.',
                  f'- Tamaños tipográficos medidos: {c["min_font_pt"]}–{c["max_font_pt"]} pt (incluye numeraciones e ilustraciones).']
        if item['view']=='visual':
            lines += [f'- QR: enlace correcto {c["qr_correct_linkedin"]}; contactos correctos {c["qr_contains_contacts"]}; decodificación a 300 dpi {c["qr_decoded_at_300dpi"]}; lado {c["qr_size_mm"]} mm.',
                      f'- Descripciones de trayectoria: {l["fieldSizes"][".hito-desc"]*options.scale*.75:.2f} pt; herramientas: {l["fieldSizes"][".tool-tag"]*options.scale*.75:.2f} pt.',
                      '- Diseño en dos columnas: conserva riesgo residual de interpretación en algunos ATS. La copia lineal reduce ese riesgo sin omitir contenido.']
        lines+=['']
    lines+=['## Alcance de las pruebas','',
            'Se verifica integridad de frases, caracteres, fuentes, orden de experiencias, tamaño de archivo, A4 y QR. No se certifica PDF/UA, PDF/A ni aprobación en ATS. La lectura del QR en papel y teléfono físico queda pendiente.','',
            'Fuentes de criterios externos: https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse ; https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-formats-for-resumes-cover-letters-and-other-candidate-uploads .']
    (PROJECT/'PDF_GENERATION_REPORT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')


def main():
    options=args();process=None;results=[];logs=None
    try:
        if Path(options.out).name!=options.out or not options.out.lower().endswith('.pdf'):raise ValueError('--out debe ser un nombre PDF, sin rutas.')
        if not 0.1<=options.scale<=2:raise ValueError('Escala fuera de rango.')
        if not shutil.which('node') or not shutil.which('npm'):raise RuntimeError('Falta Node/npm. En macOS: brew install node; luego npm ci.')
        if not (PROJECT/'node_modules').is_dir():raise RuntimeError('Faltan dependencias Node. Ejecuta npm ci.')
        if options.desktop and not (Path.home()/'Desktop').is_dir():raise RuntimeError('No existe ~/Desktop en este equipo. No se creará un Escritorio ficticio.')
        print('[INFO] Compilando el proyecto gobernado...')
        subprocess.run(['npm','run','build'],cwd=PROJECT,check=True)
        data=read_data(PROJECT);dist=PROJECT/'dist';url=None
        if not options.offline:
            with socket.socket() as test:
                if test.connect_ex(('127.0.0.1',options.port))==0:raise RuntimeError(f'Puerto {options.port} ocupado. Cierra el preview anterior o usa --port.')
            logs=(dist/'preview.log').open('w')
            process=subprocess.Popen(['node','node_modules/vite/bin/vite.js','preview','--host','127.0.0.1','--port',str(options.port),'--strictPort'],cwd=PROJECT,stdout=logs,stderr=subprocess.STDOUT)
            deadline=time.monotonic()+45
            while time.monotonic()<deadline:
                if process.poll() is not None:raise RuntimeError('Vite Preview terminó antes de estar disponible.')
                with socket.socket() as test:
                    if test.connect_ex(('127.0.0.1',options.port))==0:break
                time.sleep(.2)
            else:raise RuntimeError('Vite Preview no respondió.')
            url=f'http://127.0.0.1:{options.port}/'
        with sync_playwright() as pw:
            executable=os.environ.get('CV_CHROMIUM_PATH')
            browser=pw.chromium.launch(headless=True,**({'executable_path':executable} if executable else {}))
            try:
                results.append(generate(browser,PROJECT,data,dist/options.out,options,'visual',url))
                if options.with_ats:results.append(generate(browser,PROJECT,data,dist/ATS_NAME,options,'ats',url))
            finally:browser.close()
        report(results,options)
        # Solo publicar cuando TODAS las verificaciones solicitadas han finalizado bien.
        for item in results:
            output=dist/item['file'];atomic_copy(output,PROJECT/output.name)
            if options.desktop:atomic_copy(output,Path.home()/'Desktop'/output.name)
            print(f'[OK] {output.name}: {item["checks"]["pages"]} página(s), {item["checks"]["bytes"]/1024:.1f} KB, contenido íntegro.')
        if options.desktop:print('[OK] Copias verificadas en '+str(Path.home()/'Desktop'))
        if not options.no_open and sys.platform=='darwin':subprocess.run(['open',str(PROJECT/options.out)],check=False)
        print('[OK] PDF_GENERATION_REPORT.md actualizado. No se ha ejecutado un ATS comercial.')
    except Exception as exc:
        report(results,options,str(exc));print('[ERROR]',exc,file=sys.stderr);return 1
    finally:
        if process:
            process.terminate()
            try:process.wait(timeout=5)
            except subprocess.TimeoutExpired:process.kill()
        if logs:logs.close()
    return 0

if __name__=='__main__':sys.exit(main())
