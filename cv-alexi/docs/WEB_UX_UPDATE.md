# UX y cursos UC — 2026-10-12

Actualización solicitada por Alexi sobre el diseño web aprobado.

## Alcance
- Entradas sutiles de contenido: 360 ms, máximo 10 px, una sola vez. El texto nunca parte oculto.
- Respuesta visual en enlaces, botones y menú, sin carruseles, parallax, contadores ni nuevas dependencias.
- Indicador discreto de avance, sección activa, anclas con foco y retorno al inicio.
- Menú compacto hasta 960 px; Escape, cierre al navegar y por salida de foco.
- Respeto de prefers-reduced-motion tanto en CSS como en JavaScript, cambio en vivo y control manual por sesión.
- Dos enlaces visibles a cursos UC, con target=_blank, noopener noreferrer y aviso de nueva pestaña. URLs proporcionadas por el usuario conservadas literalmente, incluido seccion_id=9083.

## Aislamiento
No se modifican src/data.js, src/App.jsx del PDF, src/styles.css del PDF, generate_pdf.py ni las imágenes. Todos los indicadores, nueve experiencias y 40 herramientas siguen presentes. El contacto público continúa siendo LinkedIn.

## Comprobación reproducible
Desde cv-alexi:
```
node scripts/build_web.mjs
python scripts/check_web_ux.py
python scripts/check_web_ux.py --url https://cv-alexi.vercel.app --out web-review/ux-production
```
Informe JSON y capturas: artefacto CV_WEB_UX del workflow Validate CV web UX. La prueba de apertura de cursos usa interceptación para comprobar URL, teclado y pestaña nueva sin realizar una matrícula. Las páginas oficiales también fueron localizadas mediante consulta pública.

La revisión local del build y de la composición se realizó antes del commit. La navegación por red se verifica en GitHub Actions porque el navegador del entorno local bloquea las direcciones locales. El reporte del workflow, no esta descripción, determina el resultado final de las pruebas. No se declara certificación WCAG completa.

Criterios de movimiento: https://www.w3.org/WAI/WCAG22/Techniques/css/C39 y https://www.w3.org/WAI/WCAG21/Techniques/client-side-script/SCR40 .
