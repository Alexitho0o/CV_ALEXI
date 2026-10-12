"""QA de interacción web. --url permite verificar el mismo despliegue público.
No modifica datos, archivos PDF ni configuración Git/Vercel.
"""
from __future__ import annotations
import argparse, functools, http.server, json, os, subprocess, threading
from pathlib import Path
from playwright.sync_api import sync_playwright

PROJECT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--url')
parser.add_argument('--out', default=str(PROJECT / 'web-review' / 'ux'))
args = parser.parse_args()
out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
server = None
if args.url:
    url = args.url.rstrip('/')
else:
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *_): pass
    handler = functools.partial(Quiet, directory=str(PROJECT / 'web-dist'))
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f'http://127.0.0.1:{server.server_port}'
links = {
    'bodega': 'https://educacioncontinua.uc.cl/programas/gestion-eficiente-de-bodegas-y-control-de-inventario/?seccion_id=9083',
    'compras': 'https://educacioncontinua.uc.cl/programas/gestion-en-compras-y-adquisiciones/',
}
expected = json.loads(subprocess.check_output(['node','--input-type=module','-e',
    "import * as d from './src/data.js';console.log(JSON.stringify({title:d.profile.title,summary:d.profile.summary,experiences:d.trayectoria,tools:d.toolGroups.flatMap(g=>g.items),private:[d.profile.phone,d.profile.email]}))"], cwd=PROJECT))
errors = []; results = []; checks = {}

def check(ok, label):
    if not ok: errors.append(label)

def inspect(page):
    return page.evaluate('''() => {
      const fields=[...document.querySelectorAll('h1,h2,h3,h4,p,[data-tool],.hero-title,.experience-date,.course-link strong')];
      return {width:innerWidth,scrollWidth:document.documentElement.scrollWidth,
        kpis:document.querySelectorAll('.kpi').length,experiences:document.querySelectorAll('.experience').length,
        tools:document.querySelectorAll('[data-tool]').length,courses:document.querySelectorAll('[data-course]').length,
        images:document.images.length,failedImages:[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src),
        clipped:fields.filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>e.textContent),
        invalidAnchors:[...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.getElementById(a.hash.slice(1))).map(a=>a.hash),
        links:[...document.querySelectorAll('[data-course]')].map(a=>({id:a.dataset.course,href:a.href,target:a.target,rel:a.rel,label:a.getAttribute('aria-label')})),
        descriptions:[...document.querySelectorAll('.experience-desc')].map(e=>e.textContent),
        toolNames:[...document.querySelectorAll('[data-tool]')].map(e=>e.textContent),
        html:document.documentElement.outerHTML};
    }''')

def load(page, suffix=''):
    response = page.goto(url+suffix, wait_until='networkidle')
    check(response and response.status == 200, f'HTTP {suffix}')
    page.evaluate('document.querySelectorAll("img").forEach(i=>i.loading="eager")')
    page.evaluate('async()=>{await document.fonts.ready; await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})))}')
    page.wait_for_timeout(420)

try:
    with sync_playwright() as pw:
        options = {'headless': True}
        if os.environ.get('CHROMIUM_EXECUTABLE'):
            options['executable_path'] = os.environ['CHROMIUM_EXECUTABLE']
        browser = pw.chromium.launch(**options)
        version = browser.version
        for width in [320,375,390,650,768,960,1024,1440,1920]:
            page = browser.new_page(viewport={'width':width,'height':1000})
            page.on('pageerror', lambda e: errors.append(str(e)))
            load(page)
            data = inspect(page)
            check(data['scrollWidth']<=width+1 and not data['clipped'] and not data['failedImages'] and not data['invalidAnchors'], f'Layout {width}: {data.get("clipped")}')
            check((data['kpis'], data['experiences'], data['tools'], data['courses'])==(8,9,40,2), f'Contenido {width}')
            check(data.pop('descriptions')==[h['desc'] for h in expected['experiences']],f'Descripciones completas {width}')
            check(data.pop('toolNames')==expected['tools'],f'Herramientas completas {width}')
            html = data.pop('html')
            check(not any(v in html for v in expected['private']),f'Privacidad {width}')
            for link in data['links']:
                check(link['href']==links[link['id']] and link['target']=='_blank' and 'noopener' in link['rel'] and 'pestaña nueva' in link['label'],f'Enlace {width}: {link}')
            if width<=960:
                page.locator('.menu-toggle').click()
                check(page.locator('.menu-toggle').get_attribute('aria-expanded')=='true',f'Abrir menú {width}')
                page.keyboard.press('Escape')
                check(page.locator('.menu-toggle').get_attribute('aria-expanded')=='false',f'Escape {width}')
                check(page.locator('.menu-toggle').evaluate('(e)=>e===document.activeElement'),f'Foco de menú {width}')
                page.locator('.menu-toggle').click()
            page.locator('[data-nav="cursos-uc"]').click()
            page.wait_for_timeout(1200)
            check(page.locator('#cursos-uc').evaluate('(e)=>e===document.activeElement'),f'Foco ancla cursos {width}')
            check(page.locator('.menu-toggle').get_attribute('aria-expanded')=='false',f'Cerrar menú al navegar {width}')
            y=page.locator('#cursos-uc').bounding_box()['y']
            header_height=page.locator('.site-header').bounding_box()['height']
            check(header_height-2<=y<=header_height+42, f'Posición de ancla {width}: {y}')
            check(page.locator('[data-nav="cursos-uc"]').get_attribute('aria-current')=='location',f'Sección activa {width}')
            if width in (390,1440):
                page.screenshot(path=str(out/f'ux-{width}-cursos.png'))
                page.locator('.back-to-top').click()
                page.wait_for_timeout(1200)
                page.screenshot(path=str(out/f'ux-{width}-inicio.png'))
                check(page.locator('#inicio').evaluate('(e)=>e===document.activeElement'),f'Regreso inicio {width}')
            results.append(data);page.close()
        # Apertura de enlaces con teclado: interceptada para no invocar servicios externos.
        page=browser.new_page(viewport={'width':1440,'height':1000})
        page.context.route('https://educacioncontinua.uc.cl/**', lambda r:r.fulfill(status=200,content_type='text/html',body='<title>UC: destino verificado</title>'))
        load(page)
        for key in links:
            page.locator(f'[data-course="{key}"]').focus()
            with page.expect_popup() as info: page.keyboard.press('Enter')
            popup=info.value;popup.wait_for_load_state()
            check(popup.url==links[key],f'URL popup {key}')
            check(popup.evaluate('window.opener===null'),f'Noopener {key}')
            popup.close()
        checks['keyboardCourseLinks']=True
        # Prueba de animación real y cancelación inmediata por preferencia del sistema.
        load(page)
        page.evaluate('''() => { window.uxAnimationCalls=[]; const original=Element.prototype.animate;
          Element.prototype.animate=function(frames,opts){window.uxAnimationCalls.push(opts); return original.call(this,frames,opts);};
          document.getElementById('impacto').scrollIntoView({behavior:'instant'}); }''')
        page.wait_for_timeout(50)
        check(len(page.evaluate('window.uxAnimationCalls'))>0,'Animaciones ejecutadas al entrar')
        page.emulate_media(reduced_motion='reduce');page.wait_for_timeout(40)
        check(page.evaluate('document.getAnimations().length')==0,'Cancelación movimiento reducido')
        checks['motionCancelledOnPreferenceChange']=True
        page.close()
        page=browser.new_page(viewport={'width':390,'height':900},reduced_motion='reduce')
        load(page)
        page.locator('.menu-toggle').click()
        check(page.evaluate('document.getAnimations().length')==0,'Menú movimiento reducido')
        check(page.locator('[data-motion-toggle]').is_disabled(),'Respeta configuración del sistema')
        check(page.evaluate('getComputedStyle(document.documentElement).scrollBehavior')=='auto','Scroll reducido')
        checks['reducedMotion']=True;page.close()
        page=browser.new_page(viewport={'width':1440,'height':1000})
        load(page)
        page.locator('[data-motion-toggle]').click()
        check(page.locator('html').get_attribute('class').find('reduced-motion')>=0,'Control de animaciones')
        page.reload(wait_until='networkidle')
        check(page.locator('[data-motion-toggle]').get_attribute('aria-pressed')=='true','Preferencia por sesión')
        checks['sessionMotionControl']=True;page.close()
        page=browser.new_page(viewport={'width':390,'height':900},java_script_enabled=False)
        load(page);d=inspect(page)
        check(d['experiences']==9 and d['tools']==40 and d['courses']==2 and d['scrollWidth']<=391,'Sin JavaScript')
        check(page.locator('[data-nav="cursos-uc"]').is_visible(),'Navegación sin JavaScript')
        checks['withoutJavaScript']=True;page.close()
        page=browser.new_page(viewport={'width':390,'height':900})
        page.add_init_script('delete window.IntersectionObserver; delete window.ResizeObserver;')
        page.on('pageerror', lambda e:errors.append(str(e)))
        load(page)
        check(page.locator('[data-course]').count()==2,'Fallback sin observadores')
        checks['withoutObservers']=True;page.close()
        page=browser.new_page(viewport={'width':390,'height':900})
        page.route('**/img/FOTO.png',lambda r:r.abort())
        load(page)
        check(page.locator('.hero-photo .image-fallback').is_visible(),'Fallback de foto')
        checks['imageFallback']=True;page.close()
        browser.close()
finally:
    if server: server.shutdown()
report={'url':url,'browser':version,'viewports':results,'checks':checks,'errors':errors,
        'coursePopupTest':'Destinos exactos y pestaña nueva probados mediante interceptación, no matrícula real.',
        'pdfSourcesUnchanged':json.loads((PROJECT/'WEB_BUILD_REPORT.json').read_text())['pdfSourcesUnchanged'] if (PROJECT/'WEB_BUILD_REPORT.json').exists() else None}
(out/'WEB_UX_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'errors':errors,'checks':checks,'widths':[v['width'] for v in results]},ensure_ascii=False,indent=2))
if errors: raise SystemExit(1)
