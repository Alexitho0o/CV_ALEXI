# pages/5_Contacto.py
# -*- coding: utf-8 -*-
import streamlit as st

from services.contact_service import submit_contact_form
from shared.cv_content import DATOS_PERSONALES
from shared.ui_components import render_page_header, render_quick_links

st.set_page_config(page_title="Contacto - Alexi Burgos CV", page_icon="📧", layout="wide")

# CSS
st.markdown("""
<style>
.contact-hero {
    background: linear-gradient(135deg, #0891b2 0%, #06b6d4 100%);
    color: white;
    padding: 3rem 2rem;
    border-radius: 16px;
    margin-bottom: 2rem;
    text-align: center;
    box-shadow: 0 10px 30px rgba(8,145,178,0.2);
}
.contact-hero h1 {
    font-size: 2.5rem;
    font-weight: 900;
    margin-bottom: 0.5rem;
}
.contact-hero p {
    font-size: 1.1rem;
    margin: 0;
}
.contact-card {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    border: 2px solid #e2e8f0;
    margin: 1.5rem 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    transition: all 0.3s ease;
}
.contact-card:hover {
    border-color: #0891b2;
    box-shadow: 0 4px 16px rgba(8,145,178,0.1);
    transform: translateY(-2px);
}
.contact-label {
    font-size: 0.9rem;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.5rem;
    font-weight: 600;
}
.contact-value {
    font-size: 1.2rem;
    color: #0f172a;
    font-weight: 600;
    word-break: break-all;
}
.contact-value a {
    color: #0891b2;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.2s ease;
    border-bottom: 2px solid transparent;
    display: inline-block;
}
.contact-value a:hover {
    color: #0284c7;
    border-bottom: 2px solid #0891b2;
}
.icon {
    font-size: 1.8rem;
    margin-right: 0.5rem;
}
.contact-form {
    background: linear-gradient(135deg, #f8fafc 0%, white 100%);
    padding: 2rem;
    border-radius: 12px;
    margin: 2rem 0;
}
.button-group {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

render_page_header(
    "📬 Contacto",
    "¡Estoy disponible para colaboraciones y oportunidades profesionales!",
    "linear-gradient(135deg, #0891b2 0%, #06b6d4 100%)",
)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("## 📞 Datos de Contacto")
    
    contact_html = f"""
    <div class="contact-card">
        <div class="contact-label">📞 Teléfono</div>
        <div class="contact-value"><a href="tel:+56945130486">{DATOS_PERSONALES['TELEFONO']}</a></div>
    </div>
    
    <div class="contact-card">
        <div class="contact-label">📧 Correo Electrónico</div>
        <div class="contact-value"><a href="mailto:{DATOS_PERSONALES['CORREO']}">{DATOS_PERSONALES['CORREO']}</a></div>
    </div>
    
    <div class="contact-card">
        <div class="contact-label">📍 Ubicación</div>
        <div class="contact-value">{DATOS_PERSONALES['UBICACION']}</div>
    </div>
    
    <div class="contact-card">
        <div class="contact-label">💼 LinkedIn</div>
        <div class="contact-value"><a href="https://www.linkedin.com/in/alexiburgos" target="_blank">linkedin.com/in/alexiburgos ↗</a></div>
    </div>
    """
    
    st.markdown(contact_html, unsafe_allow_html=True)

with col2:
    st.markdown("## 🎯 Disponibilidad")
    
    availab_html = """
    <div class="contact-card">
        <div class="contact-label">📍 Modalidad</div>
        <div class="contact-value">
            ✅ En línea únicamente
        </div>
    </div>
    
    <div class="contact-card">
        <div class="contact-label">🕒 Horario disponible</div>
        <div class="contact-value">
            Mar–Jue 21:30 en adelante<br>
            Vie 17:30–23:00<br>
            Sáb 08:00–17:00
        </div>
    </div>
    """
    
    st.markdown(availab_html, unsafe_allow_html=True)

st.divider()

st.markdown("## 💬 Áreas de Interés")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 📊 Data & Analytics
    - Power BI
    - Análisis de datos
    - Reportes estratégicos
    - Business Intelligence
    """)

with col2:
    st.markdown("""
    ### 🎓 Educación
    - Gestión académica
    - Análisis institucional
    - Acreditación
    - Mejora continua
    """)

with col3:
    st.markdown("""
    ### 📦 Logística
    - Gestión de operaciones
    - Control de inventarios
    - Compras estratégicas
    - Supply chain
    """)

st.divider()

st.markdown("## 📝 Formulario de Contacto")

with st.form("contact_form"):
    nombre = st.text_input("Tu nombre", placeholder="Ej: Juan Pérez")
    email = st.text_input("Tu correo", placeholder="tu@email.com")
    asunto = st.selectbox("Asunto", [
        "Oportunidad de empleo",
        "Proyecto/Colaboración",
        "Consultoría",
        "Docencia/Capacitación",
        "Otra consulta"
    ])
    mensaje = st.text_area("Mensaje", placeholder="Cuéntame tu propuesta...", height=150)
    
    submitted = st.form_submit_button("📧 Enviar Mensaje", use_container_width=True)
    
    if submitted:
        exito, respuesta = submit_contact_form(nombre, email, asunto, mensaje)

        if exito:
            st.success(f"""
            {respuesta}
            
            **Detalles del contacto:**
            - Nombre: {nombre.strip()}
            - Correo: {email.strip()}
            - Asunto: {asunto}
            """)
        else:
            st.error(respuesta)

st.divider()

st.markdown("## 🔗 Enlaces Rápidos")
render_quick_links(
    DATOS_PERSONALES["CORREO"],
    DATOS_PERSONALES["TELEFONO"],
    "https://linkedin.com/in/alexiburgos",
)

st.divider()

st.markdown("### ⏱️ Horarios de Disponibilidad")

schedule_html = """
<div style="background: linear-gradient(135deg, #f8fafc 0%, white 100%); padding: 1.5rem; border-radius: 12px; border-left: 4px solid #0891b2;">
    <strong>Lunes a Viernes:</strong> 9:00 - 18:00 (Hora de Chile)<br>
    <strong>Sábados:</strong> Disponible para consultas urgentes<br>
    <strong>Domingos:</strong> Descanso
</div>
"""

st.markdown(schedule_html, unsafe_allow_html=True)
