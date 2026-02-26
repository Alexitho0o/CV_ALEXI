# pages/6_Competencias.py
# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(page_title="Competencias - Alexi Burgos CV", page_icon="🎯", layout="wide")

COMPETENCIAS = {
    "Gestión Académica y Tecnológica": (
        "Integración de TIC, TAC y TEP en la coordinación y gestión de procesos académicos y administrativos. "
        "Uso de tecnologías avanzadas para la planificación, evaluación y seguimiento de los aprendizajes esperados, "
        "garantizando calidad y efectividad en su implementación. Colaboración proactiva en equipos interdisciplinarios "
        "a través de plataformas digitales, asegurando la integración de recursos tecnológicos para potenciar la educación "
        "y el desarrollo profesional."
    ),
    "Metodologías y Evaluación": (
        "Modelo por competencias, metodologías de enseñanza y evaluación, diseño y validación de instrumentos de levantamiento "
        "de datos para la toma de decisiones y la mejora continua. Diseño y medición de indicadores clave de desempeño (KPI) "
        "para evaluar la efectividad de programas y procesos educativos."
    ),
    "Conocimientos Específicos": (
        "Comprensión profunda de la normativa, políticas y procedimientos que rigen los procesos educativos en la Educación "
        "Superior en Chile."
    ),
}

# CSS
st.markdown("""
<style>
.hero-header {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: white;
    padding: 3rem 2rem;
    border-radius: 16px;
    margin-bottom: 2rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.hero-header h1 {
    font-size: 2.5rem;
    font-weight: 900;
    margin-bottom: 0.5rem;
}

.hero-sub {
    color: #cbd5e1;
    font-size: 1rem;
    margin: 0.5rem 0;
    font-weight: 500;
}

.competencia-card {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    margin: 1.5rem 0;
    border-left: 4px solid #0891b2;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    transition: all 0.3s ease;
}

.competencia-card:hover {
    box-shadow: 0 8px 20px rgba(8,145,178,0.15);
    transform: translateY(-2px);
}

.competencia-title {
    font-size: 1.3rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #0891b2;
}

.competencia-text {
    color: #475569;
    line-height: 1.8;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

header_gradient = "linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%)"
st.markdown(f"""
<div style="background: {header_gradient}; color: white; padding: 3rem 2rem; border-radius: 16px; margin-bottom: 2rem; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
    <h1>🎯 Competencias Profesionales</h1>
    <p>Fortalezas y áreas de especialización</p>
</div>
""", unsafe_allow_html=True)

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
