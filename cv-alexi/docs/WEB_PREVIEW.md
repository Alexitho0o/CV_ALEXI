# Vista web ejecutiva — propuesta sin alterar el PDF

Fuente: `src/data.js` de la revisión aprobada `ee0eedc2c85b16f900f5cdca0019844c44253606`.

## Separación de salidas

- PDF: `src/App.jsx`, `src/styles.css`, `generate_pdf.py` y `dist/`. No se modifican.
- Web: `src/web/App.jsx`, `src/web/styles.css`, `src/web/enhance.js` y `web-dist/`.
- Compilación: `node scripts/build_web.mjs`, desde `cv-alexi/`.
- Vista local: `python3 -m http.server 8080 --directory web-dist`.
- Pruebas de navegador: `python3 scripts/check_web.py` (Playwright/Chromium instalado).

La web conserva los 8 indicadores, 9 experiencias con sus descripciones completas y las 40 herramientas. No se usa el PDF como imagen ni iframe. React genera HTML estático con texto desde los mismos datos antes de enviar la página al navegador. El JavaScript del cliente solo mejora navegación y recuperación ante errores de imágenes.

## Publicación y privacidad

La rama `feat/cv-web-ejecutivo` es una propuesta. No fusionar sin aprobación visual del usuario. `vercel.json` dirige la compilación web y publica solo `web-dist`, no la raíz del repositorio. Los PDF con contacto personal, vCards, respaldos y fuentes internas no se copian al sitio. LinkedIn se mantiene como contacto público, respetando las decisiones previas de privacidad. El PDF aprobado no cambia ni se publica automáticamente.

Las rutas antiguas de experiencia, educación, habilidades y contacto redirigen a sus secciones. Competencias redirige a Áreas clave. Equipamiento y referencias no forman parte de la ficha aprobada y sus rutas remiten a Contacto; no se publica información adicional de terceros.

## Verificación

El build contrasta título, resumen, cargos, instituciones, subtítulos, descripciones y herramientas con `data.js`. Genera `WEB_BUILD_REPORT.json` y compara SHA-256 de las cinco fuentes del PDF antes/después. La CI prueba 8 anchos, menú móvil, navegación interna, imágenes, desbordamiento, contenido sin JavaScript y fallback de foto. Los informes y capturas quedan en el artefacto `CV_WEB_PREVIEW`. Una prueba automática no sustituye la aprobación visual.
