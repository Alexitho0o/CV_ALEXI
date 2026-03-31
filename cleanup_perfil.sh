#!/bin/bash
# Script para eliminar archivos de Perfil
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}/pages"
rm -f 1_Perfil.py _MERGED_Perfil_Backup.py _1_Perfil_DISABLED.py
echo "✅ Archivos eliminados"
ls -la | grep -i perfil || echo "✅ No hay archivos de Perfil restantes"
