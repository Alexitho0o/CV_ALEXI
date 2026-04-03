# 📄 CV — Alexi Burgos (HTML)

Este repositorio contiene un **CV estático** en HTML con diseño responsivo y recursos estáticos.
Incluye un **dashboard de habilidades** con **Chart.js** y un formulario de contacto basado en **EmailJS**.

## Cómo Ejecutarlo

1. Abre el archivo `html/index.html` o `index.html` en cualquier navegador web.

## Despliegue

1. **GitHub Pages**:
   - Sube el contenido del proyecto a un repositorio en GitHub.
   - Ve a la configuración del repositorio y habilita GitHub Pages en la rama `main`.
   - Accede al CV desde la URL proporcionada por GitHub Pages.

2. **Netlify**:
   - Arrastra y suelta el contenido del proyecto en la interfaz de Netlify.
   - Netlify generará automáticamente una URL para tu CV.

3. **Vercel**:
   - Sube el proyecto a Vercel y selecciona la carpeta raíz como punto de inicio.

## Notas Finales

- Asegúrate de que los archivos `css/styles.css` y `js/app.js` estén minificados para un mejor rendimiento.
- Si usas `EmailJS` en el formulario de contacto, revisa `html/contacto.html` y configura las claves públicas/privadas que requiere ese servicio.

## Problemas comunes

- Evita subir credenciales en texto plano: archivos como `.env` deben mantenerse fuera del repositorio público.

## Comandos útiles de despliegue

```bash
# Redeploy manual: push a main
git push origin main
```

## Dependencias del Proyecto (recursos estáticos)

### CSS
- **Bootstrap**: Archivo: `css/bootstrap.min.css`

### JavaScript
- **Chart.js**: Archivo: `js/chart.min.js`

---

Si necesitas que vuelva a eliminar artefactos Python (tests, workflows adicionales) o deje instrucciones para GitHub Pages/Netlify más detalladas, dímelo y lo dejo listo.