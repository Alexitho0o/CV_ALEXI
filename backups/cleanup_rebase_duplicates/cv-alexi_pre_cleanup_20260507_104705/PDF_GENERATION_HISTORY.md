# Historial de fases — CV Alexi Marcelo Burgos Flores

> Este archivo preserva el historial de fases de desarrollo.
> `PDF_GENERATION_REPORT.md` es sobrescrito en cada generación — este archivo es permanente.

---

## FASE 10 — Corrección visual fina (2026-04-30)

- Quickfacts sidebar limpiado (sin sub-líneas numéricas)
- KPI signos corregidos: `+1` AÑO EN UC, `+1` AÑO ANALÍTICA, `+216` CAPACITADOS UC
- Trayectoria expandida de 7 a 9 entradas individuales
- `catColors` como fuente única de verdad para colores de categoría
- Logos trayectoria: 28px → 40px
- Instituciones docentes: grilla 2×2 debajo de Formación
- Círculos Modelo de Impacto: 42px → 50px

---

## FASE 11 — Enriquecimiento de trayectoria y layout (2026-04-30)

- Formación reducida a 3 entradas validadas (eliminada "Certificación en Docencia — En proceso")
- Trayectoria: `cat` string → `cats` array; períodos con mes+año; campo `desc` por hito
- Santo Tomás: `cats: ['COORDINACIÓN', 'DOCENCIA']`
- IPSS: (en FASE 12 corregido a `['ANALÍTICA', 'DOCENCIA']`)
- Columna período: 72px → 100px
- Nuevas clases: `.hito-cats`, `.hito-desc`
- Modelo de Impacto: full-width (eliminado grid 2 columnas con quote al lado)
- QuoteBar: nuevo banner horizontal full-width debajo del modelo
- PDF resultado: 1 página A4, 5056.7 KB, Alto .cv = 1081 px

---

## FASE 12 — Gobernanza documental y auditoría de contenido (2026-04-30)

- Creados: `docs/fuentes/CV_FUENTE_EXTRACTO.md`, `CV_FUENTE_ESTRUCTURADO.json`, `CV_FUENTE_MAPA.md`, `CV_FUENTE_TRAYECTORIA.tsv`
- Creado: `docs/PROJECT_GOVERNANCE.md`
- Corrección IPSS: `cats` actualizado a `['ANALÍTICA', 'DOCENCIA']` (cargo fuente: "Analista de Datos Institucional - Docente")
- PDF resultado: 1 página A4, 5057.3 KB, Alto .cv = 1081 px

---

## FASE 13 — Auditoría intensiva batch 800 + ITERACIÓN 801 (2026-04-30)

- Análisis de 800 iteraciones internas, sin cambios en archivos
- Diagnóstico: BUENO PERO REQUIERE FASE 14
- Problemas críticos identificados:
  - C1: Orden cronológico incorrecto ENAC/Escuela de Comercio
  - C2: `.hito-desc` 0.52rem → ~5.9px en print (microtexto)
  - C3: `generate_pdf.py` sobreescribe reporte (historial perdido)
- Problemas adicionales: KPI "6+" vs fuente "7"; KPIs internos sin validar; código muerto CSS/JS

---

## FASE 14 — Correcciones quirúrgicas según ITERACIÓN 801 (2026-05-01)

### Cambios aplicados

| Archivo | Cambio |
|---|---|
| `src/data.js` | Swap trayectoria índices 3 y 4: Escuela de Comercio (Mar. 2023) ahora aparece antes que ENAC (Mar. 2022) |
| `src/data.js` | KPI gestión educativa: `'6+'` → `'7+'`, `'AÑOS DOCENCIA'` → `'AÑOS GESTIÓN EDUCATIVA'`, texto actualizado |
| `src/styles.css` | `.hito-desc font-size`: `0.52rem` → `0.57rem` (legibilidad en impresión) |
| `src/styles.css` | `.footer-link font-size`: `0.58rem` → `0.64rem` |
| `src/styles.css` | `.cl font-size`: `0.59rem` → `0.64rem` |
| `src/styles.css` | Variables muertas eliminadas: `--navy2`, `--logistica` |
| `src/styles.css` | Variable nueva: `--textd: #4b5563` (color `.hito-desc`) |
| `src/styles.css` | `.hito-desc color`: `#4b5563` → `var(--textd)` |
| `src/App.jsx` | Imports muertos eliminados: `Briefcase`, `Monitor`, `Clock` |
| `src/App.jsx` | `IconMap`: eliminadas entradas `Briefcase`, `Monitor`, `Clock` |
| `docs/fuentes/CV_FUENTE_ESTRUCTURADO.json` | KPIs internos marcados como "validado por usuario en FASE 14" |

### Validaciones

- ✅ PDF generado en 1 página A4
- ✅ Alto .cv = 1092 px (97.3% de A4 — 30px de incremento por desc más grande + footer más grande)
- ✅ 15 imágenes, 0 errores
- ✅ Sin overflow horizontal
- ✅ Escuela de Comercio (Mar. 2023) ahora aparece antes de ENAC (Mar. 2022)
- ✅ KPI gestión educativa = 7+ (alineado con fuente gobernada)
- ✅ KPI internos documentados como validados por usuario
- ✅ Sin rediseño visual
- ✅ Código muerto eliminado (verificado por grep antes de eliminar)

### Nota sobre archivos backup en src/

Se detectaron archivos backup: `src/App 2.jsx`, `src/data 2.js`, `src/data 3.js`, `src/styles 2.css`, `src/styles 3.css`. No se eliminaron (no solicitado en FASE 14). Vite no los incluye en el build. Pueden limpiarse en una fase posterior si se decide.
