#!/usr/bin/env python3
"""
generate_pdf.py — Exporta el CV Visual a PDF con Playwright.

Uso:
  python3 generate_pdf.py                      # dev server o lo inicia
  python3 generate_pdf.py --scale 0.71         # ajustar escala
  python3 generate_pdf.py --preview            # build + preview (más estable)
  python3 generate_pdf.py --preview --scale 0.68

Dependencias Python:
  pip install playwright pypdf
  python -m playwright install chromium

Dependencias Node:
  npm install   (solo si node_modules no existe)
"""

import argparse
import datetime
import os
import shutil
import socket
import subprocess
import sys
import threading
import time

# ── Auto-bootstrap: reiniciar con venv si playwright no disponible ──
VENV_PY = "/Users/alexi/venv/bin/python3"
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    if os.path.exists(VENV_PY) and os.path.abspath(sys.executable) != os.path.abspath(VENV_PY):
        os.execv(VENV_PY, [VENV_PY] + sys.argv)
    print("[ERROR] playwright no disponible.")
    print("  pip install playwright")
    print("  python -m playwright install chromium")
    sys.exit(1)

# ── Constantes ──────────────────────────────────────────────────────
PROJECT_DIR  = os.path.dirname(os.path.abspath(__file__))
DIST_DIR     = os.path.join(PROJECT_DIR, "dist")
OUTPUT_NAME  = "CV_Alexi_Marcelo_Burgos_Flores_visual.pdf"
OUTPUT_PDF   = os.path.join(DIST_DIR, OUTPUT_NAME)
OUTPUT_ROOT  = os.path.join(PROJECT_DIR, OUTPUT_NAME)
REPORT_PATH  = os.path.join(PROJECT_DIR, "PDF_GENERATION_REPORT.md")

DEV_PORT     = 5173
PREVIEW_PORT = 4173

# A4 portrait a 96 dpi = 793.7 × 1122.5 px
# El CV está diseñado a 1120px ancho → escala = 793.7 / 1120 ≈ 0.709
# Bajar si el PDF tiene más de 1 página; subir si queda con mucho espacio vacío
DEFAULT_SCALE = 0.709

REQUIRED_SELECTORS = [".cv", ".cv-hero", ".cv-kpi", ".cv-footer"]

# ── Colores de terminal ──────────────────────────────────────────────
GRN = "\033[0;32m"
RED = "\033[0;31m"
YLW = "\033[0;33m"
CYN = "\033[0;36m"
BLD = "\033[1m"
RST = "\033[0m"

def ok(msg):   print(f"  {GRN}[OK]{RST}   {msg}")
def err(msg):  print(f"  {RED}[ERROR]{RST} {msg}")
def warn(msg): print(f"  {YLW}[WARN]{RST}  {msg}")
def info(msg): print(f"  {CYN}[INFO]{RST}  {msg}")


# ════════════════════════════════════════════════════════════════════
# ARGUMENTOS
# ════════════════════════════════════════════════════════════════════
def parse_args():
    p = argparse.ArgumentParser(
        description="Genera PDF del CV Visual (A4, 1 página)"
    )
    p.add_argument(
        "--scale", type=float, default=DEFAULT_SCALE,
        help=f"Factor de escala de impresión CSS (default: {DEFAULT_SCALE})"
    )
    p.add_argument(
        "--out", default=None,
        help=f"Nombre del PDF de salida (default: {OUTPUT_NAME})"
    )
    p.add_argument(
        "--preview", action="store_true",
        help="Usar npm run build + preview en vez del servidor dev"
    )
    return p.parse_args()


# ════════════════════════════════════════════════════════════════════
# DEPENDENCIAS
# ════════════════════════════════════════════════════════════════════
def find_bin(name):
    for prefix in ("/usr/local/bin", "/opt/homebrew/bin", "/opt/local/bin"):
        candidate = os.path.join(prefix, name)
        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate
    return shutil.which(name)


def check_node_deps():
    node = find_bin("node")
    npm  = find_bin("npm")
    if not node:
        err("'node' no encontrado. Instala Node.js:")
        err("  brew install node")
        sys.exit(1)
    if not npm:
        err("'npm' no encontrado.")
        sys.exit(1)
    node_modules = os.path.join(PROJECT_DIR, "node_modules")
    if not os.path.isdir(node_modules):
        err("node_modules no existe. Ejecuta primero:")
        err("  npm install")
        sys.exit(1)
    ok(f"node  → {node}")
    ok(f"npm   → {npm}")
    return node, npm


# ════════════════════════════════════════════════════════════════════
# SERVIDOR
# ════════════════════════════════════════════════════════════════════
def port_open(port):
    try:
        for res in socket.getaddrinfo("localhost", port, socket.AF_UNSPEC, socket.SOCK_STREAM):
            af, stype, proto, _cname, sa = res
            try:
                with socket.socket(af, stype, proto) as s:
                    s.settimeout(0.5)
                    if s.connect_ex(sa) == 0:
                        return True
            except OSError:
                continue
    except OSError:
        pass
    return False


def wait_for_server(port, timeout_s=60):
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        if port_open(port):
            return True
        time.sleep(0.5)
    return False


def _drain_proc(proc, lines):
    for raw in proc.stdout:
        lines.append(raw.decode("utf-8", errors="replace").rstrip())


def start_dev_server():
    info("Iniciando servidor Vite dev...")
    vite_bin = os.path.join(PROJECT_DIR, "node_modules", ".bin", "vite")
    proc = subprocess.Popen(
        [vite_bin, "--host", "127.0.0.1"],
        cwd=PROJECT_DIR,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    lines = []
    threading.Thread(target=_drain_proc, args=(proc, lines), daemon=True).start()
    if not wait_for_server(DEV_PORT):
        err("Servidor dev no respondió en 60 s.")
        print("\n".join(lines[:30]))
        proc.terminate()
        sys.exit(1)
    ok(f"Dev server activo en http://localhost:{DEV_PORT}")
    return proc, f"http://localhost:{DEV_PORT}"


def start_preview_server(npm):
    info("Ejecutando npm run build...")
    result = subprocess.run(
        [npm, "run", "build"],
        cwd=PROJECT_DIR,
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        err("Build falló:")
        print(result.stdout[-3000:])
        print(result.stderr[-3000:])
        sys.exit(1)
    ok("Build completado")

    info("Iniciando servidor preview...")
    vite_bin = os.path.join(PROJECT_DIR, "node_modules", ".bin", "vite")
    proc = subprocess.Popen(
        [vite_bin, "preview", "--host", "127.0.0.1"],
        cwd=PROJECT_DIR,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    lines = []
    threading.Thread(target=_drain_proc, args=(proc, lines), daemon=True).start()
    if not wait_for_server(PREVIEW_PORT):
        err("Servidor preview no respondió en 60 s.")
        print("\n".join(lines[:30]))
        proc.terminate()
        sys.exit(1)
    ok(f"Preview server activo en http://localhost:{PREVIEW_PORT}")
    return proc, f"http://localhost:{PREVIEW_PORT}"


# ════════════════════════════════════════════════════════════════════
# VALIDACIÓN DE LAYOUT EN NAVEGADOR
# ════════════════════════════════════════════════════════════════════
def check_layout(page):
    info("Verificando layout en navegador...")
    report = page.evaluate("""
    () => {
        const cv        = document.querySelector('.cv');
        const cvRect    = cv ? cv.getBoundingClientRect() : null;
        const imgs      = Array.from(document.images);
        const failed    = imgs.filter(i => !i.complete || i.naturalWidth === 0);
        const overflowX = document.documentElement.scrollWidth >
                          document.documentElement.clientWidth + 2;
        return {
            hasCv:      !!cv,
            hasHero:    !!document.querySelector('.cv-hero'),
            hasKpi:     !!document.querySelector('.cv-kpi'),
            hasFooter:  !!document.querySelector('.cv-footer'),
            hasQr:      !!document.querySelector('.qr-img'),
            hasPhoto:   !!document.querySelector('.photo'),
            cvWidth:    cvRect ? Math.round(cvRect.width)  : null,
            cvHeight:   cvRect ? Math.round(cvRect.height) : null,
            scrollW:    document.documentElement.scrollWidth,
            scrollH:    document.documentElement.scrollHeight,
            clientW:    document.documentElement.clientWidth,
            clientH:    document.documentElement.clientHeight,
            totalImgs:  imgs.length,
            failedImgs: failed.length,
            overflowX:  overflowX,
        };
    }
    """)

    def tick(v): return "✓" if v else "✗"

    print()
    print(f"  {'─' * 42}")
    print(f"  Layout check (media print):")
    print(f"    .cv presente        {tick(report['hasCv'])}")
    print(f"    .hero presente      {tick(report['hasHero'])}")
    print(f"    .kpi-grid presente  {tick(report['hasKpi'])}")
    print(f"    .cv-footer presente {tick(report['hasFooter'])}")
    print(f"    QR imagen           {tick(report['hasQr'])}")
    print(f"    Foto perfil         {tick(report['hasPhoto'])}")
    print(f"    Ancho .cv           {report['cvWidth']} px")
    print(f"    Alto .cv            {report['cvHeight']} px")
    print(f"    scrollWidth         {report['scrollW']} px")
    print(f"    scrollHeight        {report['scrollH']} px")
    print(f"    Imágenes totales    {report['totalImgs']}")
    print(f"    Imágenes con error  {report['failedImgs']}")
    print(f"    Overflow horizontal {'⚠  SÍ' if report['overflowX'] else 'no'}")
    print(f"  {'─' * 42}")
    print()

    if not report["hasCv"]:
        err("No se encontró el selector .cv en la página. Abortando.")
        sys.exit(1)
    if report["overflowX"]:
        warn("Overflow horizontal detectado. El PDF podría quedar cortado lateralmente.")
    if report["failedImgs"] > 0:
        warn(f"{report['failedImgs']} imagen(es) no cargaron (se usará fallback de texto).")

    return report


# ════════════════════════════════════════════════════════════════════
# GENERACIÓN DE PDF
# ════════════════════════════════════════════════════════════════════
def generate_pdf(url, scale, output_path):
    os.makedirs(DIST_DIR, exist_ok=True)
    layout_report = {}

    with sync_playwright() as pw:
        info("Lanzando Chromium (headless)...")
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1200, "height": 1600},
            device_scale_factor=1,
        )
        page = context.new_page()

        info(f"Cargando {url} ...")
        page.goto(url, wait_until="networkidle", timeout=45_000)

        # 1. Inyectar la variable de escala ANTES de emular print
        #    para que @media print vea el valor correcto al aplicar zoom
        info(f"Aplicando --print-scale: {scale} ...")
        page.evaluate(
            f"document.documentElement.style.setProperty('--print-scale', '{scale}')"
        )

        # 2. Esperar fuentes e imágenes completamente cargadas
        info("Esperando fuentes e imagenes...")
        page.evaluate("""
            async () => {
                await document.fonts.ready;
                const imgs = Array.from(document.images);
                await Promise.all(imgs.map(img => {
                    if (img.complete) return Promise.resolve();
                    return new Promise(resolve => {
                        img.onload = img.onerror = resolve;
                    });
                }));
            }
        """)

        # 3. Cambiar a media print para activar @media print y zoom
        page.emulate_media(media="print")

        # 4. Pausa corta para que el layout con zoom se estabilice
        page.wait_for_timeout(600)

        # 5. Validar layout en modo print
        layout_report = check_layout(page)

        # 6. Generar PDF
        info("Generando PDF A4...")
        page.pdf(
            path=output_path,
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            scale=1.0,
        )
        browser.close()

    return layout_report


# ════════════════════════════════════════════════════════════════════
# VALIDACIÓN DE PÁGINAS DEL PDF
# ════════════════════════════════════════════════════════════════════
def validate_pdf_pages(pdf_path):
    """Devuelve el número de páginas del PDF, o None si no hay librería disponible."""
    try:
        import pypdf
        reader = pypdf.PdfReader(pdf_path)
        return len(reader.pages)
    except ImportError:
        pass

    try:
        import PyPDF2
        with open(pdf_path, "rb") as f:
            return len(PyPDF2.PdfReader(f).pages)
    except ImportError:
        pass

    try:
        import fitz
        doc = fitz.open(pdf_path)
        n = doc.page_count
        doc.close()
        return n
    except ImportError:
        pass

    warn("No se encontró pypdf / PyPDF2 / pymupdf para contar páginas.")
    warn("  pip install pypdf")
    return None


# ════════════════════════════════════════════════════════════════════
# REPORTE MARKDOWN
# ════════════════════════════════════════════════════════════════════
def write_report(pdf_path, url, scale, page_count, layout_report, errors, method):
    now      = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    size_kb  = os.path.getsize(pdf_path) / 1024 if os.path.isfile(pdf_path) else 0
    page_ok  = page_count == 1

    def chk(v): return "✅" if v else "❌"

    lines = [
        "# PDF Generation Report",
        "",
        f"**Generado:** {now}  ",
        f"**Archivo:** `{pdf_path}`  ",
        f"**Tamaño:** {size_kb:.1f} KB  ",
        f"**Páginas:** {page_count if page_count is not None else 'N/A'} "
        f"{'✅' if page_ok else '❌ (se esperaba 1)'}  ",
        f"**URL usada:** {url}  ",
        f"**Método:** {method}  ",
        f"**Escala CSS:** {scale}  ",
        f"**Formato:** A4 portrait · 793.7 × 1122.5 px @ 96 dpi  ",
        "",
        "## Layout check (en navegador, antes de imprimir)",
        "",
        "| Elemento | Estado |",
        "|---|:---:|",
        f"| `.cv` presente | {chk(layout_report.get('hasCv'))} |",
        f"| `.cv-hero` presente | {chk(layout_report.get('hasHero'))} |",
        f"| `.cv-kpi` presente | {chk(layout_report.get('hasKpi'))} |",
        f"| `.cv-footer` presente | {chk(layout_report.get('hasFooter'))} |",
        f"| QR imagen | {chk(layout_report.get('hasQr'))} |",
        f"| Foto perfil | {chk(layout_report.get('hasPhoto'))} |",
        f"| Overflow horizontal | {'❌ detectado' if layout_report.get('overflowX') else '✅ no'} |",
        "",
        f"**Ancho .cv:** {layout_report.get('cvWidth', 'N/A')} px  ",
        f"**Alto .cv:** {layout_report.get('cvHeight', 'N/A')} px  ",
        f"**scrollWidth:** {layout_report.get('scrollW', 'N/A')} px  ",
        f"**scrollHeight:** {layout_report.get('scrollH', 'N/A')} px  ",
        f"**Imágenes totales:** {layout_report.get('totalImgs', 'N/A')}  ",
        f"**Imágenes con error:** {layout_report.get('failedImgs', 'N/A')}  ",
        "",
    ]

    if errors:
        lines += ["## Errores detectados", ""]
        for e in errors:
            lines.append(f"- {e}")
        lines.append("")

    if not page_ok and page_count:
        new_scale = round(scale - 0.02, 3)
        lines += [
            "## Recomendaciones (contenido desborda A4)",
            "",
            f"El PDF tiene **{page_count} páginas**. El contenido supera el alto de A4.",
            "Prueba reducir la escala:",
            "",
            "```bash",
            f"python3 generate_pdf.py --scale {new_scale}",
            f"python3 generate_pdf.py --preview --scale {new_scale}",
            "```",
            "",
            "Si el problema persiste, reducir padding/gap en el CSS para compactar secciones.",
        ]
    else:
        lines += [
            "## Resultado",
            "",
            "✅ PDF generado correctamente en **1 página A4**.",
            "",
            "Para regenerar:",
            "```bash",
            f"python3 generate_pdf.py --scale {scale}",
            "```",
        ]

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    ok(f"Reporte: {REPORT_PATH}")


# ════════════════════════════════════════════════════════════════════
# ABRIR PDF CON LA APLICACIÓN DEL SISTEMA
# ════════════════════════════════════════════════════════════════════
def open_pdf(pdf_path):
    """Abre el PDF con el visor predeterminado del sistema operativo."""
    openers = {"darwin": "open", "win32": "explorer"}
    cmd = openers.get(sys.platform, "xdg-open")
    try:
        subprocess.Popen([cmd, pdf_path])
        ok("PDF abierto en el visor del sistema")
    except Exception as exc:
        warn(f"No se pudo abrir el PDF automáticamente: {exc}")


# ════════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════════
def main():
    args = parse_args()
    scale = args.scale

    out_name = args.out or OUTPUT_NAME
    out_path = os.path.join(DIST_DIR, out_name)
    out_root = os.path.join(PROJECT_DIR, out_name)

    print()
    print(f"{BLD}══════════════════════════════════════════════{RST}")
    print(f"{BLD}  CV Visual — Generador de PDF (A4)          {RST}")
    print(f"{BLD}══════════════════════════════════════════════{RST}")
    print()
    info(f"Escala:  {scale}")
    info(f"Modo:    {'build + preview' if args.preview else 'dev server'}")
    info(f"Salida:  {out_path}")
    print()

    server_proc   = None
    url           = None
    method        = ""
    errors        = []
    layout_report = {}

    try:
        # ── Servidor ──────────────────────────────────────────────
        if args.preview:
            _, npm = check_node_deps()
            server_proc, url = start_preview_server(npm)
            method = "preview server (npm run build + preview)"
        else:
            if port_open(DEV_PORT):
                ok(f"Dev server ya activo en http://localhost:{DEV_PORT}")
                url    = f"http://localhost:{DEV_PORT}"
                method = "dev server (externo, ya en ejecución)"
            else:
                check_node_deps()
                server_proc, url = start_dev_server()
                method = "dev server (iniciado por este script)"

        print()

        # ── Generar PDF ───────────────────────────────────────────
        layout_report = generate_pdf(url, scale, out_path)

    except KeyboardInterrupt:
        print()
        err("Interrumpido por el usuario.")
        sys.exit(1)
    except Exception as exc:
        err(f"Error al generar PDF: {exc}")
        errors.append(str(exc))
        if server_proc:
            server_proc.terminate()
        sys.exit(1)
    finally:
        if server_proc:
            server_proc.terminate()
            server_proc.wait()
            info("Servidor detenido")

    # ── Verificar archivo ─────────────────────────────────────────
    print()
    if not os.path.isfile(out_path):
        err("El PDF no fue creado.")
        sys.exit(1)

    size_kb = os.path.getsize(out_path) / 1024
    ok(f"PDF creado  → {out_path}  ({size_kb:.1f} KB)")

    # Copia en raíz del proyecto para acceso rápido
    shutil.copy2(out_path, out_root)
    ok(f"Copia raíz → {out_root}")

    # ── Validar páginas ───────────────────────────────────────────
    page_count = validate_pdf_pages(out_path)
    if page_count is None:
        warn("No se pudo validar páginas (instala pypdf: pip install pypdf).")
    elif page_count == 1:
        ok("Páginas: 1 ✓ — PDF en una sola hoja A4")
    else:
        err(f"Páginas: {page_count} — El contenido desborda A4.")
        errors.append(f"PDF con {page_count} páginas (se esperaba 1)")
        warn("Prueba reducir la escala:")
        new_s = round(scale - 0.02, 3)
        print(f"    python3 generate_pdf.py --scale {new_s}")
        print(f"    python3 generate_pdf.py --preview --scale {new_s}")

    # ── Reporte ───────────────────────────────────────────────────
    write_report(out_path, url, scale, page_count, layout_report, errors, method)

    # ── Resumen final ─────────────────────────────────────────────
    print()
    print(f"{BLD}══════════════════════════════════════════════{RST}")
    ok("Generación completada")
    print(f"  PDF dist:  {BLD}{out_path}{RST}")
    print(f"  PDF raíz:  {BLD}{out_root}{RST}")
    print(f"  Escala:    {BLD}{scale}{RST}")
    print(f"  Páginas:   {BLD}{page_count if page_count is not None else 'N/A'}{RST}")
    print(f"{BLD}══════════════════════════════════════════════{RST}")
    print()
    if page_count == 1:
        print("  Si el CV se ve bien, no hace falta ajustar nada.")
    else:
        print(f"  Ajustar escala:  python3 generate_pdf.py --scale {round(scale - 0.02, 3)}")
    print()

    # ── Abrir PDF automáticamente ─────────────────────────────────
    open_pdf(out_path)

    if page_count is not None and page_count != 1:
        sys.exit(2)


if __name__ == "__main__":
    main()
