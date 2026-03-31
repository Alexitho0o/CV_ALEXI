# pages/4_Educacion.py
# -*- coding: utf-8 -*-
import streamlit as st

from shared.cv_content import EDUCACION
from shared.ui_components import EXECUTIVE_HEADER_GRADIENT, render_page_header

st.set_page_config(page_title="Educación - Alexi Burgos CV", page_icon="🎓", layout="wide")

IDIOMAS = "Inglés técnico"

# CSS
st.markdown("""
<style>
.education-item {
    background: #FFFFFF;
    padding: 1.55rem;
    border-radius: 12px;
    border: 1px solid #CBD5E1;
    border-left: 4px solid #0E7490;
    margin: 1rem 0;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.07);
}
.degree {
    font-size: 1.08rem;
    font-weight: 900;
    color: #0F172A;
    margin-bottom: 0.35rem;
}
.institution {
    font-size: 0.95rem;
    color: #475569;
    margin-bottom: 0.3rem;
}
.year {
    font-size: 0.86rem;
    color: #0E7490;
    font-weight: 700;
    display: inline-block;
    background: #F1F5F9;
    border: 1px solid #CBD5E1;
    padding: 0.34rem 0.74rem;
    border-radius: 999px;
    margin-top: 0.5rem;
}
.language-box {
    background: #FFFFFF;
    color: #0F172A;
    padding: 1.4rem;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #CBD5E1;
    border-left: 4px solid #1E3A8A;
    box-shadow: 0 8px 20px rgba(15, 23, 42, 0.07);
}
.language-box h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1.1rem;
}
.language-box p {
    margin: 0;
    font-weight: 600;
    font-size: 1rem;
    color: #475569;
}
</style>
""", unsafe_allow_html=True)

# header
header_gradient = EXECUTIVE_HEADER_GRADIENT
render_page_header(
    "Educación y Formación",
    "*Formación profesional y postítulo en logística, educación y analítica*",
    header_gradient,
)

st.divider()

st.markdown("## 📚 Títulos y Formación de Postítulo")

for degree, institution, years in EDUCACION:
    icono = "🏆 " if degree.startswith("Título") else "📘 "
    edu_html = f"""
    <div class="education-item">
        <div class="degree">{icono}{degree}</div>
        <div class="institution">{institution}</div>
        <div class="year">{years}</div>
    </div>
    """
    st.markdown(edu_html, unsafe_allow_html=True)

st.divider()

st.markdown("## 🌐 Idiomas")

lang_html = f"""
<div class="language-box">
    <h3>🗣️ {IDIOMAS}</h3>
    <p>Nivel: Técnico/Profesional</p>
</div>
"""

st.markdown(lang_html, unsafe_allow_html=True)

st.divider()

st.markdown("## 🎯 Certificaciones y Cursos")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Actuales")
    st.markdown("""
    - 🏅 Análisis de Datos (en progreso)
    - 📊 Power BI Avanzado (en progreso)
    - 🎓 Evaluación Educativa (completado)
    """)

with col2:
    st.markdown("### Especialidades")
    st.markdown("""
    - Análisis Institucional
    - Gestión Académica
    - Mejora Continua
    - Business Intelligence
    - Educación Superior
    """)

st.divider()

st.markdown("## 📊 Resumen Formativo")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Títulos Obtenidos", "2")
    
with col2:
    st.metric("Postítulos", "1")
    
with col3:
    st.metric("Años de Estudio", "7+")

st.divider()

st.markdown("### 🎯 Áreas de Estudio")
st.markdown("""
✅ **Logística y Operaciones**: Gestión de cadenas de suministro, control de inventarios, compras estratégicas

✅ **Análisis y Datos**: Estadística, modelamiento de datos, BI y visualización

✅ **Educación**: Medición y evaluación de aprendizajes, gestión académica, acreditación
""")
