# pages/4_Educacion.py
# -*- coding: utf-8 -*-
import streamlit as st

from shared.cv_content import EDUCACION
from shared.ui_components import render_page_header

st.set_page_config(page_title="Educación - Alexi Burgos CV", page_icon="🎓", layout="wide")

IDIOMAS = "Inglés técnico"

# CSS
st.markdown("""
<style>
.education-item {
    background: linear-gradient(135deg, #f8fafc 0%, white 100%);
    padding: 2rem;
    border-radius: 12px;
    border-top: 5px solid #0891b2;
    margin: 1.5rem 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.degree {
    font-size: 1.2rem;
    font-weight: 900;
    color: #0f172a;
    margin-bottom: 0.5rem;
}
.institution {
    font-size: 1rem;
    color: #64748b;
    margin-bottom: 0.3rem;
}
.year {
    font-size: 0.95rem;
    color: #0891b2;
    font-weight: 700;
    display: inline-block;
    background: rgba(8,145,178,0.1);
    padding: 0.4rem 1rem;
    border-radius: 20px;
    margin-top: 0.5rem;
}
.language-box {
    background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
    color: white;
    padding: 2rem;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(124,58,237,0.2);
}
.language-box h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1.3rem;
}
.language-box p {
    margin: 0;
    font-weight: 600;
    font-size: 1.1rem;
}
</style>
""", unsafe_allow_html=True)

# header
header_gradient = "linear-gradient(135deg, #ef4444 0%, #f87171 100%)"
render_page_header(
    "🎓 Educación y Formación",
    "*Formación académica en logística, educación y análisis de datos*",
    header_gradient,
)

st.divider()

st.markdown("## 📚 Formación Académica")

for degree, institution, years in EDUCACION:
    edu_html = f"""
    <div class="education-item">
        <div class="degree">{'🏆 ' if 'Titulado' in degree else '📖 '}{degree}</div>
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

st.markdown("## 📊 Resumen Académico")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Grados Obtenidos", "3")
    
with col2:
    st.metric("Años de Estudio", "7+")
    
with col3:
    st.metric("Especialidades", "2")

st.divider()

st.markdown("### 🎯 Áreas de Estudio")
st.markdown("""
✅ **Logística y Operaciones**: Gestión de cadenas de suministro, control de inventarios, compras estratégicas

✅ **Análisis y Datos**: Estadística, modelamiento de datos, BI y visualización

✅ **Educación**: Medición y evaluación de aprendizajes, gestión académica, acreditación
""")
