# Mapa de fuente CV — Alexi Marcelo Burgos Flores

> Navegación rápida del documento fuente. No releer el PDF completo para cada modificación.
> Versión: 1.0 — 2026-04-30

---

## Dónde está cada tipo de dato

| Tipo de dato | Fuente / sección en PDF | Archivo gobernado | Clave o ID |
|---|---|---|---|
| Contacto | Identificación (página 1) | CV_FUENTE_ESTRUCTURADO.json | `persona` |
| Perfil | Perfil profesional (página 1) | CV_FUENTE_ESTRUCTURADO.json | `perfil_profesional` |
| Docente UC | Experiencia laboral (página 1) | CV_FUENTE_ESTRUCTURADO.json | `exp_001` |
| IPSS | Experiencia laboral (página 1) | CV_FUENTE_ESTRUCTURADO.json | `exp_002` |
| CFT PUCV | Experiencia laboral (página 1) | CV_FUENTE_ESTRUCTURADO.json | `exp_003` |
| Escuela de Comercio | Experiencia laboral (página 2) | CV_FUENTE_ESTRUCTURADO.json | `exp_005` |
| ENAC | Experiencia laboral (página 2) | CV_FUENTE_ESTRUCTURADO.json | `exp_004` |
| Santo Tomás | Experiencia laboral (página 2) | CV_FUENTE_ESTRUCTURADO.json | `exp_006` |
| Hotel Plaza San Francisco | Experiencia laboral (página 2) | CV_FUENTE_ESTRUCTURADO.json | `exp_007` |
| GK | Experiencia laboral (página 2) | CV_FUENTE_ESTRUCTURADO.json | `exp_008` |
| Experiencia inicial bodega 2012–2015 | Experiencia laboral (páginas 2–3) | CV_FUENTE_ESTRUCTURADO.json | `exp_009` |
| Formación | Educación (página 3) | CV_FUENTE_ESTRUCTURADO.json | `formacion` |
| Herramientas | Habilidades (página 3) | CV_FUENTE_ESTRUCTURADO.json | `herramientas` |
| Competencias | Competencias (página 3) | CV_FUENTE_EXTRACTO.md | Sección Competencias |
| Equipamiento | Equipamiento (página 3) | CV_FUENTE_ESTRUCTURADO.json | `equipamiento` |
| Referencias | Referencias (página 4) | CV_FUENTE_ESTRUCTURADO.json | `referencias` |
| Datos por validar | — | CV_FUENTE_ESTRUCTURADO.json | `datos_no_validados_o_por_revisar` |

---

## Mapa de IDs de experiencia (cronología inversa)

| ID | Institución | Período fuente | Categoría(s) |
|---|---|---|---|
| exp_001 | Pontificia Universidad Católica de Chile | Jul. 2025 – Actualidad | DOCENCIA |
| exp_002 | Instituto Profesional San Sebastián | May. 2025 – Actualidad | ANALÍTICA, DOCENCIA |
| exp_003 | CFT PUCV | Mar. 2024 – Ene. 2025 | COORDINACIÓN |
| exp_005 | IP-CFT Escuela de Comercio de Santiago | Mar. 2023 – May. 2024 | DOCENCIA |
| exp_004 | CFT ENAC | Mar. 2022 – Mar. 2024 | DOCENCIA |
| exp_006 | IP-CFT Santo Tomás | Ago. 2019 – Mar. 2024 (dos sedes) | COORDINACIÓN, DOCENCIA |
| exp_007 | Hotel Plaza San Francisco | Ago. 2018 – Abr. 2019 | LOGÍSTICA |
| exp_008 | Sociedad Importadora y Comercializadora GK | Jul. 2015 – Ene. 2018 | LOGÍSTICA |
| exp_009 | La Polar · Amphora · Computación Integral · Casa Ximena | May. 2012 – Jun. 2015 | LOGÍSTICA |

---

## Mapa de formación

| ID | Programa | Institución | Período |
|---|---|---|---|
| edu_001 | Ingeniería en Gestión de Operaciones Logísticas | Instituto Profesional AIEP | 2023–2025 |
| edu_002 | Diplomado en Medición y Evaluación de Aprendizajes | PUC / Escuela de Psicología | Oct. 2022 – May. 2023 |
| edu_003 | Técnico de Nivel Superior en Logística | CFT PUCV | 2013–2015 |

---

## Reglas de uso de esta fuente

1. Para modificar datos del CV visual, revisar primero `CV_FUENTE_ESTRUCTURADO.json`.
2. Si el dato no está en el JSON, revisar `CV_FUENTE_EXTRACTO.md`.
3. Si el dato tampoco está ahí, marcar como `"por validar"` en `datos_no_validados_o_por_revisar`.
4. No usar memoria ni supuestos para completar datos.
5. No releer el PDF completo salvo que el mapa indique una inconsistencia o que el usuario adjunte una nueva versión.
6. Toda corrección posterior debe indicar qué ID del JSON respalda el cambio.

---

## Notas de auditoría (FASE 12)

| Hito | Estado en data.js | Concordancia con fuente |
|---|---|---|
| UC (exp_001) | ✅ cats: ['DOCENCIA'] | Correcto |
| IPSS (exp_002) | ⚠️ cats: ['ANALÍTICA'] solo | **Corregido en FASE 12** → ['ANALÍTICA', 'DOCENCIA'] |
| CFT PUCV (exp_003) | ✅ cats: ['COORDINACIÓN'] | Correcto |
| ENAC (exp_004) | ✅ cats: ['DOCENCIA'] | Correcto |
| Escuela de Comercio (exp_005) | ✅ cats: ['DOCENCIA'] | Correcto |
| Santo Tomás (exp_006) | ✅ cats: ['COORDINACIÓN', 'DOCENCIA'] | Correcto |
| Hotel (exp_007) | ✅ cats: ['LOGÍSTICA'] | Correcto |
| GK (exp_008) | ✅ cats: ['LOGÍSTICA'] | Correcto |
| Bloque 2012–2015 (exp_009) | ✅ cats: ['LOGÍSTICA'] | Correcto |
| edu_001 (AIEP) | ✅ | Correcto |
| edu_002 (Diplomado PUC) | ✅ (institución abreviada válida) | Correcto |
| edu_003 (CFT PUCV) | ✅ | Correcto |
