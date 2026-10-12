"""Pruebas del sitio estático, sin tocar el generador PDF ni el código de producción."""
from __future__ import annotations
import functools, http.server, json, threading, subprocess, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

PROJECT = Path(__file__).resolve().parents[1]
OUT = PROJECT / 'web-review'
OUT.mkdir(exist_ok=True)
class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_): pass
handler = functools.partial(QuietHandler, directory=str(PROJECT/'web-dist'))
server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
url = f'http://127.0.0.1:{server.server_port}'
all_results = []
errors = []
try:
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        for width in [320,375,390,650,768,1024,1440,1920]:
            page = browser.new_page(viewport={'width':width,'height':1000},device_scale_factor=1)
            page.on('pageerror',lambda e: errors.append(str(e)))
            page.goto(url,wait_until='networkidle')
            page.evaluate('document.querySelectorAll("img").forEach(i=>i.loading="eager")')
            page.evaluate('async()=>{await document.fonts.ready; await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})))}')
            check = page.evaluate('''() => {
                const fields=[...document.querySelectorAll('h1,h2,h3,p,[data-tool],.hero-title,.experience-date')];
                const clipped=fields.filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>e.textContent);
                return {width:innerWidth,scrollWidth:document.documentElement.scrollWidth,
                    kpis:document.querySelectorAll('.kpi').length,experiences:document.querySelectorAll('.experience').length,
                    tools:document.querySelectorAll('[data-tool]').length,
                    images:[...document.images].length,failedImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),
                    h1:document.querySelectorAll('h1').length,clipped,
                    allImagesNamed:[...document.images].every(i=>i.alt.length>0),
                    invalidInternalLinks:[...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.getElementById(a.hash.slice(1))).map(a=>a.hash),
                    bodyFont:parseFloat(getComputedStyle(document.querySelector('.experience-desc')).fontSize)};
            }''')
            if check['scrollWidth']>width+1 or check['failedImages'] or check['clipped'] or check['invalidInternalLinks']:
                errors.append(f'Layout {width}: {check}')
            if (check['kpis'],check['experiences'],check['tools'],check['h1']) != (8,9,40,1): errors.append(f'Contenido {width}: {check}')
            if width<=650:
                page.locator('.menu-toggle').click()
                if page.locator('.menu-toggle').get_attribute('aria-expanded')!='true': errors.append('Menú no abre')
                page.keyboard.press('Escape')
                if page.locator('.menu-toggle').get_attribute('aria-expanded')!='false': errors.append('Escape no cierra menú')
            if width in [390,768,1440]:
                page.screenshot(path=str(OUT/f'web-{width}-full.png'),full_page=True)
                page.screenshot(path=str(OUT/f'web-{width}-inicio.png'))
            all_results.append(check)
            page.close()
        page=browser.new_page(viewport={'width':390,'height':900},java_script_enabled=False)
        page.goto(url,wait_until='networkidle')
        nojs=page.evaluate('''() => ({tools:document.querySelectorAll('[data-tool]').length,experiences:document.querySelectorAll('.experience').length,scroll:document.documentElement.scrollWidth})''')
        if nojs['tools']!=40 or nojs['experiences']!=9 or nojs['scroll']>391: errors.append(f'Sin JS: {nojs}')
        page.close()
        page=browser.new_page(viewport={'width':390,'height':900})
        page.route('**/img/FOTO.png',lambda route:route.abort())
        page.goto(url,wait_until='networkidle')
        fallback_ok=page.locator('.hero-photo .image-fallback').is_visible()
        if not fallback_ok: errors.append('Fallback de foto no visible')
        browser.close()
finally:
    server.shutdown()
result={'viewports':all_results,'withoutJS':nojs,'photoFallback':fallback_ok,'errors':errors,
        'commercialATS': 'No evaluado; no corresponde a esta revisión web',
        'pdfSourcesUnchanged':json.loads((PROJECT/'WEB_BUILD_REPORT.json').read_text())['pdfSourcesUnchanged']}
(OUT/'WEB_QA_REPORT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
if errors: raise SystemExit(1)
