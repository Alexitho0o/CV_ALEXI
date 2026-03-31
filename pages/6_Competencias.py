# pages/6_Competencias.py
# -*- coding: utf-8 -*-
import streamlit as st

from shared.cv_content import COMPETENCIAS
from shared.ui_components import EXECUTIVE_HEADER_GRADIENT, render_page_header

st.set_page_config(page_title="Competencias - Alexi Burgos CV", page_icon="🎯", layout="wide")

# CSS
st.markdown("""
<style>
.competencia-card {
    background: #FFFFFF;
    padding: 1.35rem;
    border-radius: 12px;
    margin: 1rem 0;
    border: 1px solid #CBD5E1;
    border-left: 4px solid #0E7490;
    box-shadow: 0 8px 20px rgba(15, 23, 42, 0.07);
    transition: all 0.3s ease;
}

.competencia-card:hover {
    box-shadow: 0 10px 22px rgba(14, 116, 144, 0.14);
    transform: translateY(-1px);
}

.competencia-title {
    font-size: 1.1rem;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 0.75rem;
    padding-bottom: 0.45rem;
    border-bottom: 2px solid #CBD5E1;
}

.competencia-text {
    color: #475569;
    line-height: 1.68;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

header_gradient = EXECUTIVE_HEADER_GRADIENT
render_page_header(
    "Competencias Profesionales",
    "Fortalezas y áreas de especialización",
    header_gradient,
)

st.markdown("## Mis Competencias Clave")

for titulo, descripcion in COMPETENCIAS.items():
    st.markdown(f"""
    <div class="competencia-card">
        <div class="competencia-title">✓ {titulo}</div>
        <div class="competencia-text">{descripcion}</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown("### 📌 Resumen de Competencias")
st.markdown("""
Mis competencias profesionales se centran en tres pilares fundamentales:

**1. Académico-Tecnológico:** Fluidez en la integración de tecnología en procesos educativos con enfoque en TIC, TAC y TEP.

**2. Metodológico:** Expertise en diseño y validación de instrumentos, evaluación por competencias y medición de KPI para mejora continua.

**3. Normativo:** Conocimiento profundo de regulaciones y procedimientos de Educación Superior en Chile, incluyendo acreditación y SIES.
""")
