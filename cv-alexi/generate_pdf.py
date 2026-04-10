#!/usr/bin/env python3
"""
generate_pdf.py — Exporta el CV Visual a PDF con Playwright
Uso:  python3 generate_pdf.py
      python3 generate_pdf.py --scale 0.71
      python3 generate_pdf.py --out mi_cv.pdf

Requiere playwright instalado:
  pip install playwright
  python -m playwright install chromium
"""

import os
import shutil
import socket
import subprocess
import sys
import threading
import time

VENV_PY = "/Users/alexi/venv/bin/python3"
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    if os.path.exists(VENV_PY) and os.path.abspath(sys.executable) != os.path.abspath(VENV_PY):
        os.execv(VENV_PY, [VENV_PY] + sys.argv)
    print("Error: playwright no disponible.")
    print("  pip install playwright")
    print("  python -m playwright install chromium")
    sys.exit(1)

GRN = "\033[0;32m"
RED = "\033[0;31m"
YLW = "\033[0;33m"
BLD = "\033[1m"
RST = "\033[0m"

def ok(msg):   print(f"  {GRN}✓{RST} {msg}")
def err(msg):  print(f"  {RED}✗{RST} {msg}")
def info(msg): print(f"  {YLW}→{RST} {msg}")

PROJECT_DIR  = os.path.dirname(os.path.abspath(__file__))
PORT         = 5173
URL          = f"http://localhost:{PORT}"
OUTPUT_NAME  = "CV_Alexi_Marcelo_Burgos_Flores_visual.pdf"

# A4 a 96dpi = 793.7px; 793.7 / 1120 = 0.709
# Bajar si contenido se corta, subir si queda con espacio vacío
PRINT_SCALE  = 0.709

args = sys.argv[1:]
i = 0
while i < len(args):
    if args[i] == "--scale" and i + 1 < len(args):
        PRINT_SCALE = float(args[i + 1]); i += 2
    elif args[i] == "--out" and i + 1 < len(args):
        OUTPUT_NAME = args[i + 1]; i += 2
    else:
        i += 1

OUTPUT_PATH = os.path.join(PROJECT_DIR, OUTPUT_NAME)

def find_bin(name):
    for prefix in ("/usr/local/bin", "/opt/homebrew/bin", "/opt/local/bin"):
        p = os.path.join(prefix, name)
        if os.path.isfile(p) and os.access(p, os.X_OK):
            return p
    return shutil.which(name)

NODE = find_bin("node")
NPM  = find_bin("npm")

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

print()
print(f"{BLD}══════════════════════════════════════════{RST}")
print(f"{BLD}  CV Visual — Generador de PDF            {RST}")
print(f"{BLD}══════════════════════════════════════════{RST}")
print()
print(f"  Escala print:  {BLD}{PRINT_SCALE}{RST}")
print(f"  Salida:        {BLD}{OUTPUT_NAME}{RST}")
print()

vite_proc = None
server_was_running = port_open(PORT)

if server_was_running:
    ok(f"Dev server ya activo en {URL}")
else:
    if not NODE:
        err("node no encontrado.")
        sys.exit(1)

    node_modules = os.path.join(PROJECT_DIR, "node_modules", "vite")
    if not os.path.isdir(node_modules):
        info("Instalando dependencias npm...")
        subprocess.run([NPM, "install"], cwd=PROJECT_DIR, check=True)
        ok("Dependencias instaladas")

    info("Iniciando servidor Vite...")
    vite_cmd = [NODE, os.path.join(PROJECT_DIR, "node_modules", ".bin", "vite")]
    vite_proc = subprocess.Popen(
        vite_cmd, cwd=PROJECT_DIR,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )

    vite_lines = []
    def _drain():
        for raw in vite_proc.stdout:
            vite_lines.append(raw.decode("utf-8", errors="replace").rstrip())
    threading.Thread(target=_drain, daemon=True).start()

    for _ in range(60):
        time.sleep(0.5)
        if port_open(PORT):
            break
        if vite_proc.poll() is not None:
            err("Vite terminó inesperadamente:"); print("\n".join(vite_lines[:20])); sys.exit(1)
    else:
        err(f"Servidor no respondió en {URL}")
        print("\n".join(vite_lines[:20])); vite_proc.terminate(); sys.exit(1)

    ok(f"Servidor activo en {URL}")

print()

try:
    with sync_playwright() as pw:
        info("Lanzando Chromium...")
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1200, "height": 900}, device_scale_factor=1)
        page = context.new_page()

        info(f"Cargando {URL} ...")
        page.goto(URL, wait_until="networkidle", timeout=30_000)
        page.emulate_media(media="print")
        page.evaluate(
            f"document.documentElement.style.setProperty('--print-scale', '{PRINT_SCALE}')"
        )
        page.wait_for_timeout(800)
        page.evaluate("""
            () => Promise.all(
                [...document.images].map(img =>
                    img.complete ? Promise.resolve()
                    : new Promise(r => { img.onload = r; img.onerror = r; })
                )
            )
        """)

        ok("Página cargada y estilos aplicados")
        info("Generando PDF...")

        page.pdf(
            path=OUTPUT_PATH,
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            scale=1.0,
        )
        browser.close()

except Exception as e:
    err(f"Error al generar PDF: {e}")
    if vite_proc: vite_proc.terminate()
    sys.exit(1)

finally:
    if vite_proc and not server_was_running:
        vite_proc.terminate(); vite_proc.wait()
        info("Servidor Vite detenido")

if os.path.isfile(OUTPUT_PATH):
    size_kb = os.path.getsize(OUTPUT_PATH) / 1024
    print()
    print(f"{BLD}══════════════════════════════════════════{RST}")
    ok("PDF generado exitosamente")
    print(f"  Archivo: {BLD}{OUTPUT_PATH}{RST}")
    print(f"  Tamaño:  {BLD}{size_kb:.1f} KB{RST}")
    print(f"{BLD}══════════════════════════════════════════{RST}")
    print()
    print("  Si el PDF no se ve bien:")
    print("    Contenido cortado  → bajar escala:  python3 generate_pdf.py --scale 0.68")
    print("    Demasiado pequeño  → subir escala:  python3 generate_pdf.py --scale 0.73")
    print()
else:
    err("El PDF no fue creado."); sys.exit(1)
