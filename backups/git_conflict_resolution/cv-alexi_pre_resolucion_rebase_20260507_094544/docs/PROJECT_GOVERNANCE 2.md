# Gobernanza del proyecto CV — Alexi Marcelo Burgos Flores

> Versión: 1.1 — 2026-05-01
> Este documento es el punto de entrada obligatorio para cualquier modificación del CV visual.

---

## Archivos principales

| Archivo | Rol |
| --- | --- |
| `src/data.js` | Datos renderizados del CV visual |
| `src/App.jsx` | Componentes React |
| `src/styles.css` | Diseño visual |
| `generate_pdf.py` | Exportación PDF (A4, 1 página, escala 0.709) |
| `PDF_GENERATION_REPORT.md` | Reporte automático de última generación |
| `PDF_GENERATION_HISTORY.md` | Historial permanente de fases (no se sobreescribe) |
| `docs/fuentes/CV_FUENTE_ESTRUCTURADO.json` | **Fuente gobernada principal** — datos auditables por ID |
| `docs/fuentes/CV_FUENTE_EXTRACTO.md` | Texto limpio del CV fuente (PDF 4 páginas) |
| `docs/fuentes/CV_FUENTE_MAPA.md` | Mapa para ubicar datos por tipo e ID |
| `docs/fuentes/CV_FUENTE_TRAYECTORIA.tsv` | Tabla rápida de trayectoria (1 fila por hito) |

---

## Flujo obligatorio para futuras modificaciones

1. Revisar primero este archivo (`docs/PROJECT_GOVERNANCE.md`).
2. Para datos personales, experiencia, formación o herramientas → revisar `CV_FUENTE_ESTRUCTURADO.json`.
3. Para dudas de redacción o contexto → revisar `CV_FUENTE_EXTRACTO.md`.
4. Para ubicar rápidamente un dato por tipo → revisar `CV_FUENTE_MAPA.md`.
5. Para revisar fechas o categorías de trayectoria → revisar `CV_FUENTE_TRAYECTORIA.tsv`.
6. Modificar `src/data.js` solo después de validar la fuente gobernada.
7. Modificar `src/App.jsx` solo si el dato requiere ajuste de renderizado.
8. Modificar `src/styles.css` solo si hay un problema visual real.
9. Ejecutar `python3 generate_pdf.py --preview` tras cualquier cambio.
10. Actualizar `PDF_GENERATION_HISTORY.md` con un resumen de los cambios realizados.

---

## Regla de no invención

No completar datos desde memoria, inferencia o supuestos.
Todo dato debe venir de la fuente gobernada o quedar registrado como `"por validar"` en el campo `datos_no_validados_o_por_revisar` del JSON.

---

## Catálogo de categorías (catColors)

| Etiqueta | Color | Uso |
| --- | --- | --- |
| DOCENCIA | `#08284d` (navy) | Rol docente primario |
| ANALÍTICA | `#1f67c8` (blue) | Analítica de datos institucional |
| COORDINACIÓN | `#f58220` (orange) | Coordinación académica |
| LOGÍSTICA | `#2d6a8f` (petroleum blue) | Roles operativos |

Regla: las etiquetas de `catColors` son la única fuente de verdad para los colores de badges en trayectoria.

---

## Parámetros técnicos del PDF

| Parámetro | Valor |
| --- | --- |
| Ancho CV (pantalla) | 1120 px |
| Escala print | 0.709 |
| Ancho A4 resultante | ~793.7 px a 96 dpi |
| Formato | A4 portrait, 1 página |
| Motor | Chromium (Playwright) |
| Método zoom | `zoom: var(--print-scale)` en `@media print` |
| Fuentes | `document.fonts.ready` antes de captura |

---

## Historial de fases

| Fase | Descripción | Estado |
| --- | --- | --- |
| FASE 1–7 | Diseño inicial, datos, layout visual | Completado |
| FASE 8 | Auditoría técnica PDF (zoom, fonts, Playwright) | Completado |
| FASE 9 | Reporte de generación PDF | Completado |
| FASE 10 | Correcciones visuales finas (KPI, logos, colores, instituciones) | Completado |
| FASE 11 | Enriquecimiento de trayectoria (cats[], desc, QuoteBar, ImpactRow) | Completado |
| FASE 12 | Gobernanza documental y auditoría de contenido contra PDF fuente | Completado |
| FASE 13 | Auditoría intensiva batch 800 + ITERACIÓN 801 | Completado |
| FASE 14 | Correcciones quirúrgicas según ITERACIÓN 801 | Completado |

---

## Datos pendientes de validación

Ver campo `datos_no_validados_o_por_revisar` en `CV_FUENTE_ESTRUCTURADO.json`.

Items resueltos en FASE 14:

- KPI gestión educativa corregido a `7+` y documentado
- KPIs internos (1.300+ estudiantes, 55+ imparticiones, +216 capacitados UC, 12 imparticiones UC) marcados como validados por usuario
