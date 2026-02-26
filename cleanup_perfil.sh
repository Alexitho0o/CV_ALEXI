#!/bin/bash
# Script para eliminar archivos de Perfil
cd /workspaces/gdp-dashboard/pages
rm -f 1_Perfil.py _MERGED_Perfil_Backup.py _1_Perfil_DISABLED.py
echo "✅ Archivos eliminados"
ls -la | grep -i perfil || echo "✅ No hay archivos de Perfil restantes"
