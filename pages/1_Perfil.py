# pages/1_Perfil.py
# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(page_title="Perfil - Alexi Burgos CV", page_icon="👨‍💼", layout="wide")

DATOS_PERSONALES = {
    "NOMBRE": "ALEXI MARCELO BURGOS FLORES",
    "UBICACION": "Santiago, Chile",
    "TELEFONO": "+56 9 4513 0486",
    "CORREO": "alexi.fs341@gmail.com",
    "LINKEDIN": "linkedin.com/in/alexiburgos",
    "TITULO": "Docente UC | Ingeniero y Técnico en Gestión de Operaciones Logísticas",
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
    font-size: 1.1rem;
    margin: 0.5rem 0;
    font-weight: 500;
}
.info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin: 2rem 0;
}
.info-box {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    border-left: 4px solid #0891b2;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.info-box strong {
    color: #0f172a;
    font-size: 1.1rem;
}
.info-box p {
    color: #64748b;
    margin: 0.5rem 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="hero-header">
    <h1>👨‍💼 {DATOS_PERSONALES['NOMBRE']}</h1>
    <div class="hero-sub">📍 {DATOS_PERSONALES['UBICACION']}</div>
</div>
""", unsafe_allow_html=True)

st.markdown("## Información de Contacto")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="info-box">
        <strong>📞 Teléfono</strong>
        <p>{DATOS_PERSONALES['TELEFONO']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="info-box">
        <strong>🎓 Título Profesional</strong>
        <p>{DATOS_PERSONALES['TITULO']}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="info-box">
        <strong>📧 Correo</strong>
        <p>{DATOS_PERSONALES['CORREO']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="info-box">
        <strong>💼 LinkedIn</strong>
        <p>{DATOS_PERSONALES['LINKEDIN']}</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown("## 📌 Destrezas Clave")

skills_html = """
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 1.5rem 0;">
    <div style="background: #0891b2; color: white; padding: 1.5rem; border-radius: 10px; text-align: center;">
        <h3 style="margin: 0; font-size: 1rem;">📊 Análisis de Datos</h3>
        <p style="margin: 0.5rem 0; font-weight: 600;">Power BI, Excel, Python</p>
    </div>
    <div style="background: #7c3aed; color: white; padding: 1.5rem; border-radius: 10px; text-align: center;">
        <h3 style="margin: 0; font-size: 1rem;">🏫 Plataformas Educativas</h3>
        <p style="margin: 0.5rem 0; font-weight: 600;">Banner, Moodle, Blackboard</p>
    </div>
    <div style="background: #059669; color: white; padding: 1.5rem; border-radius: 10px; text-align: center;">
        <h3 style="margin: 0; font-size: 1rem;">🔧 Herramientas Ofimáticas</h3>
        <p style="margin: 0.5rem 0; font-weight: 600;">Office 365, GSuite, Kahoot</p>
    </div>
    <div style="background: #f59e0b; color: white; padding: 1.5rem; border-radius: 10px; text-align: center;">
        <h3 style="margin: 0; font-size: 1rem;">💻 Sistemas Operativos</h3>
        <p style="margin: 0.5rem 0; font-weight: 600;">MacOS, Windows, iOS, Android</p>
    </div>
    <div style="background: #ef4444; color: white; padding: 1.5rem; border-radius: 10px; text-align: center;">
        <h3 style="margin: 0; font-size: 1rem;">🌐 Idiomas</h3>
        <p style="margin: 0.5rem 0; font-weight: 600;">Inglés Técnico, Español Nativo</p>
    </div>
    <div style="background: #8b5cf6; color: white; padding: 1.5rem; border-radius: 10px; text-align: center;">
        <h3 style="margin: 0; font-size: 1rem;">🎓 Especialización</h3>
        <p style="margin: 0.5rem 0; font-weight: 600;">Logística, Educación, Datos</p>
    </div>
</div>
"""

st.markdown(skills_html, unsafe_allow_html=True)

st.divider()

st.markdown("## 🎯 Especialización")

specialization = """
Con más de **13 años en logística** y **7 años en educación superior**, soy especialista en:

- **Análisis Institucional**: Construcción de indicadores educativos
- **Gestión Académica**: Mejora continua, acreditación y calidad
- **Business Intelligence**: Desarrollo de dashboards y reportes estratégicos
- **Docencia**: Logística, Compras Estratégicas y Gestión de Operaciones
"""

st.markdown(specialization)
