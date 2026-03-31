# Auditoría técnica del repositorio (2026-03-31)

Este documento consolida un diagnóstico técnico basado en evidencia directa del código fuente actual.

## Hallazgos clave

- Proyecto Streamlit monolítico, sin backend separado ni capa de dominio reutilizable.
- Fuerte duplicación de datos de CV/experiencia/habilidades entre `cv.py` y las páginas `pages/*.py`.
- Ausencia de pruebas automatizadas y de pipeline CI/CD.
- Manejo de formulario de contacto sin validación robusta de email, rate limiting ni sanitización explícita de entradas.
- Exposición de datos personales de terceros en `pages/8_Referencias.py`.
- README desalineado respecto al estado real del repositorio (menciona `1_Perfil.py` inexistente y repo/URL heredados).

## Recomendación general

Aplicar refactor incremental orientado a:
1) centralizar datos/constantes en módulo único,
2) endurecer validaciones y seguridad del formulario,
3) introducir pruebas y quality gates,
4) ordenar arquitectura por capas para mantenibilidad.
