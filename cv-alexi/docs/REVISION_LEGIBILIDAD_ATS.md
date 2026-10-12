# Revisión de legibilidad y extracción — 2026-10-12

## Instrucciones del usuario conservadas
No modificar las cifras ni los años; no abreviar descripciones; conservar las 40 herramientas. El titular se reproduce literalmente, incluidos los dos espacios entre «IA Aplicada» y «Gestión Educativa».

## Generación gobernada
```bash
python3 -m pip install -r requirements-pdf.txt
python3 -m playwright install chromium
python3 generate_pdf.py --preview --with-ats --desktop
```
`--desktop` corresponde al Escritorio del equipo que ejecuta el comando. No se intenta acceder a un Escritorio remoto. `--offline` usa exactamente el bundle de Vite con activos incrustados para entornos que bloquean localhost. No cambia el diseño ni los datos.

La versión visual conserva una sola hoja A4. La copia LECTURA_ATS es lineal y multipágina, con el mismo contenido y cuerpo de 10 pt; no elimina herramientas ni experiencia.

## Validación
Se contrasta cada frase de los datos contra texto extraído con PyMuPDF y pypdf; cuando está instalado Poppler, también con pdftotext. Se verifica tamaño, fuentes incrustadas, Unicode, orden de las nueve experiencias, las cuarenta herramientas y la vCard correcta. El QR se prueba sobre la imagen incrustada y un recorte renderizado a 300 dpi; no equivale a una prueba con teléfono físico.

La prueba de extracción no es una certificación de ATS ni garantiza superar filtros de selección. Greenhouse documenta un límite de 2,5 MB para parsing y riesgos por columnas, gráficos, encabezados y pies; por eso se ofrece además la copia lineal. No se envía el CV a verificadores externos.

Fuentes públicas consultadas:
- https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse
- https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-formats-for-resumes-cover-letters-and-other-candidate-uploads
- https://playwright.dev/python/docs/api/class-page#page-pdf

## Preservación
CONTACTO.jpg queda como respaldo del activo original; App.jsx usa CONTACTO.png. El nuevo QR se puede regenerar desde data.js mediante `python3 scripts/generate_qr.py`. No se distribuyen archivos de fuentes.
