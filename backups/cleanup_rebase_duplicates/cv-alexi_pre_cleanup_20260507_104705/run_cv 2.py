#!/usr/bin/env python3
"""
run_cv.py — Inicia el servidor de desarrollo del CV Visual
Uso:  python3 run_cv.py
"""

import os
import shutil
import signal
import subprocess
import sys
import threading
import time
import webbrowser

PORT = 5173
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

GRN = "\033[0;32m"; RED = "\033[0;31m"; YLW = "\033[0;33m"
BLD = "\033[1m";    RST = "\033[0m"

def ok(msg):   print(f"  {GRN}✓{RST} {msg}")
def err(msg):  print(f"  {RED}✗{RST} {msg}")
def info(msg): print(f"  {YLW}→{RST} {msg}")

def find_bin(name):
    for prefix in ("/usr/local/bin", "/opt/homebrew/bin", "/opt/local/bin"):
        path = os.path.join(prefix, name)
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path
    return shutil.which(name)

NODE = find_bin("node")
NPM  = find_bin("npm")

print()
print(f"{BLD}══════════════════════════════════════════{RST}")
print(f"{BLD}  CV Visual — Servidor de desarrollo      {RST}")
print(f"{BLD}══════════════════════════════════════════{RST}")
print()

if not NODE:
    err("node no encontrado. Instalar: brew install node"); sys.exit(1)
ok(f"node  {NODE}")

if not NPM:
    err("npm no encontrado."); sys.exit(1)
ok(f"npm   {NPM}")
print()

node_modules = os.path.join(PROJECT_DIR, "node_modules", "vite")
if not os.path.isdir(node_modules):
    info("Instalando dependencias npm...")
    result = subprocess.run([NPM, "install"], cwd=PROJECT_DIR)
    if result.returncode != 0:
        err("npm install falló."); sys.exit(1)
    ok("Dependencias instaladas")
    print()

print(f"  {BLD}Iniciando servidor Vite...{RST}")
print(f"  URL: {BLD}http://localhost:{PORT}{RST}")
print(f"  Presiona {BLD}Ctrl+C{RST} para detener")
print()

vite_cmd = [NODE, os.path.join(PROJECT_DIR, "node_modules", ".bin", "vite")]
proc = subprocess.Popen(vite_cmd, cwd=PROJECT_DIR)

def _open():
    time.sleep(2.5)
    webbrowser.open(f"http://localhost:{PORT}")

threading.Thread(target=_open, daemon=True).start()

def _shutdown(sig, frame):
    print(f"\n  {YLW}Deteniendo servidor...{RST}")
    proc.terminate()
    try:    proc.wait(timeout=5)
    except: proc.kill()
    print(f"  {GRN}Servidor detenido.{RST}\n")
    sys.exit(0)

signal.signal(signal.SIGINT,  _shutdown)
signal.signal(signal.SIGTERM, _shutdown)
proc.wait()
