# 📄 CV — Alexi Burgos (Streamlit)

Este repositorio muestra un **CV estático** renderizado con **Streamlit** (sin carga de datos, sin editor, sin exportación).
Incluye un **dashboard de habilidades** dibujado con **Matplotlib** y un **formulario de contacto funcional**.

## Cómo ejecutarlo

1. Instalar dependencias

```bash
pip install -r requirements.txt
```

2. (Opcional) Configurar formulario de contacto con Gmail

Para que el formulario de contacto envíe correos a `alexi.fs341@gmail.com`:

a) Generar contraseña de aplicación en Google:
   - Ir a: https://myaccount.google.com/apppasswords
   - Necesitas 2FA (Autenticación de Dos Factores) activado
   - Seleccionar "Correo" y "Windows"
   - Google generará una contraseña de 16 caracteres

b) Crear archivo `.env` en la raíz del proyecto:

```env
GMAIL_USER=alexi.fs341@gmail.com
GMAIL_PASSWORD=xxxx xxxx xxxx xxxx
```

(Reemplaza con la contraseña generada, sin espacios)

3. Ejecutar la aplicación

```bash
streamlit run cv.py
```

La aplicación abrirá en `http://localhost:8501`

## Características

- ✅ **8 Páginas**: Perfil, Experiencia, Habilidades, Educación, Contacto, Competencias, Equipamiento, Referencias
- ✅ **Timeline Interactivo**: Visualización de trayectoria profesional con Plotly
- ✅ **Dashboard de Habilidades**: Gráfico de barras con Matplotlib
- ✅ **Contacto Interactivo**: Teléfono (tel:), Email (mailto:), LinkedIn (https://)
- ✅ **Formulario Funcional**: Envío de correos mediante SMTP de Gmail
- ✅ **Diseño Responsivo**: Bordes, colores, animaciones CSS

## Despliegue en Streamlit Cloud

Para publicar tu CV en internet de forma gratuita:

1. **Crea una cuenta** en https://streamlit.io/cloud (puedes usar tu cuenta de GitHub)

2. **Conecta tu repositorio GitHub**
   - Autoriza a Streamlit a acceder a tus repositorios
   - Selecciona este repositorio (`CV_ALEXI`)

3. **Configura los Secrets** (si usas formulario de contacto)
   - En tu app Streamlit Cloud, ve a **Settings → Secrets**
   - Agrega las siguientes líneas:
   ```toml
   GMAIL_USER = "tu_email@gmail.com"
   GMAIL_PASSWORD = "xxxx xxxx xxxx xxxx"
   ```
   - (Donde `GMAIL_PASSWORD` es tu contraseña de aplicación de Google)

4. **¡Listo!** Tu app estará disponible en:
   ```
   https://<tu-usuario>-cv-alexi.streamlit.app
   ```

### URL Pública
Una vez desplegada, comparte este URL con reclutadores y contactos. Streamlit Cloud mantiene la app corriendo 24/7 de forma gratuita.

---

## Problemas comunes

### Error: "Configuración de correo no disponible"
- Verifica que los secrets estén correctamente configurados en Streamlit Cloud
- Si trabajas localmente, verifica que `.env` exista y contenga `GMAIL_USER` y `GMAIL_PASSWORD`
- Verifica que la contraseña de aplicación no tenga espacios en código

### Error: "Error de autenticación"
- Verifica que las credenciales sean correctas
- Asegúrate de haber generado una contraseña de aplicación (no tu contraseña normal)
- Verifica que 2FA esté activado en tu cuenta de Google
- En producción (Streamlit Cloud), usa la sección **Settings → Secrets** para agregar credenciales

### La app es lenta al cargar
- Streamlit Cloud puede ser lento en conexiones de red lentas
- Los gráficos con Matplotlib se regeneran cada vez que alguien abre la página
- Esto es normal en la versión gratuita

### Comandos útiles de despliegue
```bash
# Ver logs de tu app desplegada
streamlit logs your-github-username/your-repo-name

# Redeploy manual (si cambios no se reflejan)
# Simplemente haz push a main y espera 1-2 minutos
git push origin main
```

## Estructura

```
.
├── cv.py                    # Página principal
├── shared/
│   ├── cv_content.py        # Contenido compartido del CV (fuente única)
│   └── ui_components.py     # Componentes UI reutilizables
├── services/
│   └── contact_service.py   # Validación y orquestación del formulario
├── pages/
│   ├── 2_Experiencia.py     # Timeline profesional
│   ├── 3_Habilidades.py     # Dashboard de competencias
│   ├── 4_Educacion.py       # Formación académica
│   ├── 5_Contacto.py        # Formulario de contacto
│   ├── 6_Competencias.py    # Especializaciones profesionales
│   ├── 7_Equipamiento.py    # Hardware e intereses
│   └── 8_Referencias.py     # Contactos profesionales
├── utils/
│   └── email_sender.py     # Función de envío de correos SMTP
├── requirements.txt         # Dependencias Python
├── .env                     # Variables de entorno (no commitear credenciales)
└── .env.example            # Plantilla de variables de entorno
```

## Calidad y pruebas

Comandos recomendados para validación local:

```bash
# Verificación estática básica
ruff check .

# Compilación rápida para detectar errores de sintaxis/import
python -m compileall cv.py pages utils shared services

# Pruebas unitarias
pytest -q
```

También se ejecutan automáticamente en GitHub Actions con el workflow `CI`.

## Privacidad de referencias

Los datos de contacto de referencias profesionales mostrados en la app están enmascarados en el repositorio para reducir exposición pública de información personal.
