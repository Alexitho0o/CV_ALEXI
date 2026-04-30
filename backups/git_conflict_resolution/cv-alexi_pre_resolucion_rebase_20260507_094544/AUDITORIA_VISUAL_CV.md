# Auditoría Visual CV — Alexi Marcelo Burgos Flores
**Fecha:** 2026-04-29  
**Versión:** 2.0 — Rediseño Ejecutivo Premium

---

## Diagnóstico inicial (v1)

### Problemas visuales detectados
- Nombre demasiado pequeño, sin jerarquía dominante
- Foto de tamaño insuficiente (no protagonista)
- Hero sin contraste visual fuerte (fondo blanco puro)
- Keywords como chips pequeños, difíciles de leer
- KPIs: números demasiado pequeños, tarjetas sin peso visual
- Áreas clave: bullets apretados, íconos débiles
- Logos: sin uniformidad de tamaño, nombres largos saturando
- Timeline: demasiado texto, estructura tipo tabla
- Bottom grid: columnas estrechas, texto minúsculo
- Modelo de impacto: comprimido, difícil de leer
- Quote: sin protagonismo visual
- Sensación general: ficha técnica, no ejecutivo

### Problemas técnicos detectados
- src/ no existía (archivos fuente perdidos)
- dist/img/ eliminado por Vite al fallar el build anterior
- Imágenes no estaban en public/ ni en git
- Imágenes recuperadas desde iCloud CURRICULUM/imágenes/
- package.json faltante
- vite.config.js faltante
- index.html raíz faltante

---

## Cambios aplicados (v2)

### Hero
- Fondo navy oscuro (#08284d) — contraste fuerte, look ejecutivo
- Nombre en 2 líneas, 2.35rem peso 900
- Segunda línea del nombre en azul claro (#a8c4e6) para diferenciación
- Foto 200×210px, object-fit: cover, alineada al tope
- Título en naranja (#f58220), visible y elegante
- Keywords: separador con "|" naranja, estilo tipográfico
- Resumen con interlineado generoso y color blanco suavizado
- Sidebar: 5 quick facts + QR 72px + contacto

### KPIs
- Strip independiente con borde superior navy de 3px
- Números gigantes 2.5rem peso 900
- Color top-border por KPI (navy, orange, blue)
- Ícono en caja con color fill suave
- Texto abreviado para lectura en 3 segundos

### Áreas Clave
- Tarjetas con border-top de color de área
- Íconos más grandes (d=38px)
- Bullets con dot del color del área
- Venn compacto integrado a la derecha

### Logos
- Boxes uniformes 124px ancho
- Altura fija de imagen 40px con object-fit contain
- Nombre abreviado debajo (2 líneas máx)

### Timeline
- Línea horizontal con gradiente navy→blue→orange
- Logos circulares 56px con border del color del hito
- Fechas corregidas:
  - UC: 2025 – Actualidad
  - IPSS: 2025 – Actualidad
  - CFT PUCV: 2024 – 2025
  - Docencia TP: 2019 – 2024

### Bottom Grid
- 3 columnas iguales
- Herramientas como tags con borde redondeado
- Value props con íconos naranja

### Quote
- Fondo navy, contrasta con el resto blanco
- Comilla grande naranja decorativa
- Cita en itálica blanca translúcida

### Print/PDF
- `--print-scale: 0.709` (A4 exacto a 96dpi)
- @media print: transform: scale(var(--print-scale)) desde top left
- Recomendado: `python3 generate_pdf.py --scale 0.71`

---

## Decisiones de diseño

- **Fondo hero navy**: da peso visual inmediato, diferencia de un CV en blanco
- **Foto sin recorte circular**: más ejecutivo, menos casual
- **Segunda línea del nombre en azul claro**: permite leer "ALEXI MARCELO" / "BURGOS FLORES" con jerarquía sin separar visualmente
- **KPIs arriba de Áreas**: el impacto cuantitativo va primero (reader scans top-down)
- **Herramientas como tags**: más legible y moderno que lista bulleted
- **Quote en navy**: cierra el CV con peso visual equilibrando el hero

---

## Cómo probar

```bash
# Servidor dev
python3 run_cv.py
# o directamente:
node node_modules/.bin/vite

# Abrir en navegador
http://localhost:5173
```

## Cómo exportar PDF

```bash
python3 generate_pdf.py

# Si contenido se corta:
python3 generate_pdf.py --scale 0.68

# Si queda demasiado pequeño:
python3 generate_pdf.py --scale 0.73
```

## Pendientes

- [ ] Verificar en navegador que la foto se ve bien (object-position)
- [ ] Ajustar escala de impresión si hay desborde
- [ ] Revisar que logos ENAC, Cintegral, Rhein cargan correctamente
- [ ] Confirmar QR de contacto escaneable al tamaño 72px
