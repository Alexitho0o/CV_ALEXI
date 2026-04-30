# CV Alexi Marcelo Burgos Flores — Visual

CV profesional generado con React + Vite, exportable a PDF A4 de una sola página.

## Stack

- React 19 + Vite 6
- CSS puro con variables y `@media print`
- Playwright (Python) para exportación a PDF

---

## Desarrollo

```bash
npm install
npm run dev
# → http://localhost:5173
```

---

## Generación automática de PDF

### 1. Instalar dependencias Python

```bash
pip install playwright pypdf
python -m playwright install chromium
```

### 2. Instalar dependencias Node (si no están)

```bash
npm install
```

Si Node.js no está instalado:

```bash
brew install node
npm install
```

### 3. Ejecutar

```bash
# Modo rápido: usa el servidor dev (lo inicia si no está corriendo)
python3 generate_pdf.py

# Modo estable: build + preview (recomendado para PDF final)
python3 generate_pdf.py --preview

# Ajustar escala manualmente
python3 generate_pdf.py --scale 0.70
python3 generate_pdf.py --preview --scale 0.68
```

### Resultado esperado

```
dist/CV_Alexi_Marcelo_Burgos_Flores_visual.pdf   ← archivo principal
CV_Alexi_Marcelo_Burgos_Flores_visual.pdf        ← copia en raíz
PDF_GENERATION_REPORT.md                         ← reporte de generación
```

El PDF debe ser:
- Tamaño A4 portrait (793.7 × 1122.5 px a 96 dpi)
- Exactamente 1 página
- Todo el contenido visible sin recortes ni desbordamientos

### Si el PDF tiene más de 1 página

El contenido desborda A4. Reducir la escala:

```bash
python3 generate_pdf.py --scale 0.68
python3 generate_pdf.py --preview --scale 0.68
```

### Si el PDF queda con mucho espacio vacío

El contenido es más pequeño de lo esperado. Subir la escala:

```bash
python3 generate_pdf.py --scale 0.73
```

### Escala de referencia

| Escala | Ancho resultado | Uso |
|--------|----------------|-----|
| 0.709  | ~793.7 px (A4 exacto) | Default |
| 0.68   | ~762 px | Contenido comprimido |
| 0.73   | ~818 px | Contenido expandido |

La fórmula es: `ancho_resultado = 1120 × escala`

---

## Arquitectura del CSS de impresión

El CV está diseñado a **1120 px** de ancho en pantalla.

Para exportar a A4 (793.7 px de ancho a 96 dpi), `@media print` aplica:

```css
.cv {
  zoom: var(--print-scale);   /* afecta layout, a diferencia de transform: scale */
}
```

`zoom` (a diferencia de `transform: scale`) modifica el tamaño de layout real del elemento,
lo que evita que el motor PDF de Chromium genere páginas adicionales por desbordamiento
de layout invisible.

El script inyecta el valor vía JavaScript antes de activar el modo print:
```python
page.evaluate("document.documentElement.style.setProperty('--print-scale', '0.709')")
page.emulate_media(media="print")
```

---

## Reporte de generación

Cada ejecución crea o sobreescribe `PDF_GENERATION_REPORT.md` con:

- Fecha y hora
- Archivo generado y tamaño
- Número de páginas (validado con `pypdf`)
- URL y método usado
- Escala aplicada
- Check de selectores CSS presentes
- Overflow detectado
- Imágenes cargadas / con error
- Recomendaciones si el PDF no cabe en 1 página
