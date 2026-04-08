# CV — Alexi Burgos

Sitio estático de una sola página para presentar el CV profesional de Alexi Burgos.

## Estructura actual

- `index.html`: entrada principal del sitio
- `css/styles.css`: estilos del CV
- `js/main.js`: navegación, animaciones y carga progresiva de contenido
- `experiencia.html`, `habilidades.html`, `educacion.html`, `contacto.html`, `competencias.html`, `equipamiento.html`, `referencias.html`: redirecciones a secciones internas de `index.html`

## Cómo verlo localmente

### Opción rápida

Abre `index.html` directamente en el navegador.

### Opción recomendada

Levanta un servidor estático desde la raíz del proyecto:

```bash
python3 -m http.server 8000
```

Luego abre `http://localhost:8000`.

## Despliegue

Este proyecto puede publicarse como sitio estático en GitHub Pages, Netlify o Vercel usando la raíz del repositorio como directorio público.

## Mantenimiento

- Mantén `index.html`, `css/styles.css` y `js/main.js` sincronizados: son los archivos críticos del sitio.
- Usa nombres de assets consistentes para evitar problemas de rutas entre sistemas con sensibilidad a mayúsculas/minúsculas.
- Este repositorio no necesita `.env`, credenciales ni librerías vendor locales adicionales para funcionar.
- No subas secretos ni credenciales al repositorio.
