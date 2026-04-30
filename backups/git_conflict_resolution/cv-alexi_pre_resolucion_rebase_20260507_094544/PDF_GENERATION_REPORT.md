# PDF Generation Report

<<<<<<< HEAD
**Generado:** 2026-04-30 09:12:26  
**Archivo:** `/Users/alexi/Documents/GitHub/CV_ALEXI/cv-alexi/dist/CV_Alexi_Marcelo_Burgos_Flores_visual.pdf`  
**Tamaño:** 5458.0 KB  
=======
**Generado:** 2026-05-01 00:00:13  
**Archivo:** `/Users/alexi/Documents/GitHub/CV_ALEXI/cv-alexi/dist/CV_Alexi_Marcelo_Burgos_Flores_visual.pdf`  
**Tamaño:** 5029.5 KB  
>>>>>>> 9042829 (privacy: remove phone and email from public site, keep only LinkedIn)
**Páginas:** 1 ✅  
**URL usada:** http://localhost:4173  
**Método:** preview server (npm run build + preview)  
**Escala CSS:** 0.709  
**Formato:** A4 portrait · 793.7 × 1122.5 px @ 96 dpi  

## Layout check (en navegador, antes de imprimir)

| Elemento | Estado |
|---|:---:|
| `.cv` presente | ✅ |
| `.cv-hero` presente | ✅ |
| `.cv-kpi` presente | ✅ |
| `.cv-footer` presente | ✅ |
| QR imagen | ✅ |
| Foto perfil | ✅ |
| Overflow horizontal | ✅ no |

**Ancho .cv:** 794 px  
<<<<<<< HEAD
**Alto .cv:** 748 px  
**scrollWidth:** 1200 px  
**scrollHeight:** 1600 px  
**Imágenes totales:** 14  
=======
**Alto .cv:** 1092 px  
**scrollWidth:** 1200 px  
**scrollHeight:** 1600 px  
**Imágenes totales:** 15  
>>>>>>> 9042829 (privacy: remove phone and email from public site, keep only LinkedIn)
**Imágenes con error:** 0  

## Resultado

✅ PDF generado correctamente en **1 página A4**.

<<<<<<< HEAD
Para regenerar:
```bash
python3 generate_pdf.py --scale 0.709
=======
---

## FASE 14 — Correcciones quirúrgicas (2026-05-01)

- Orden cronológico corregido: Escuela de Comercio (Mar. 2023) antes de ENAC (Mar. 2022)
- KPI gestión educativa: `6+` → `7+`, título `AÑOS GESTIÓN EDUCATIVA`
- `.hito-desc font-size`: `0.52rem` → `0.57rem` (legibilidad en impresión)
- `.footer-link` y `.cl font-size`: `0.58/0.59rem` → `0.64rem`
- Variables CSS muertas eliminadas: `--navy2`, `--logistica`
- Variable nueva: `--textd: #4b5563`
- Imports muertos eliminados de App.jsx: `Briefcase`, `Monitor`, `Clock`
- KPIs internos marcados como validados por usuario en `CV_FUENTE_ESTRUCTURADO.json`
- Alto .cv: 1081 px → 1092 px (+11 px por desc+footer más grandes, sigue en 1 página A4)
- Historial de fases: ver `PDF_GENERATION_HISTORY.md`

---

## Para regenerar

```bash
python3 generate_pdf.py --preview
>>>>>>> 9042829 (privacy: remove phone and email from public site, keep only LinkedIn)
```
