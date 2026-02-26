# pages/5_Contacto.py
# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(page_title="Contacto - Alexi Burgos CV", page_icon="📧", layout="wide")

DATOS_PERSONALES = {
    "NOMBRE": "ALEXI MARCELO BURGOS FLORES",
    "UBICACION": "Villa Alemana, Valparaíso, Chile",
    "TELEFONO": "+56 9 4513 0486",
    "CORREO": "alexi.fs341@gmail.com",
    "LINKEDIN": "linkedin.com/in/alexiburgos",
}

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

st.markdown(f"""
<div class="contact-hero">
    <h1>📬 Contacto</h1>
    <p>¡Estoy disponible para colaboraciones y oportunidades profesionales!</p>
</div>
""", unsafe_allow_html=True)

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
        <div class="contact-label">💼 Modalidades</div>
        <div class="contact-value">
            ✅ Full-time<br>
            ✅ Freelance<br>
            ✅ Part-time<br>
            ✅ Consultoría
        </div>
    </div>
    
    <div class="contact-card">
        <div class="contact-label">🌐 Ubicaciones</div>
        <div class="contact-value">
            ✅ Presencial (Santiago)<br>
            ✅ Híbrido<br>
            ✅ Remoto
        </div>
    </div>
    
    <div class="contact-card">
        <div class="contact-label">⚡ Respuesta</div>
        <div class="contact-value">
            Típicamente: 24-48 horas
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
        if nombre and email and mensaje:
            st.success(f"""
            ✅ **Mensaje registrado**
            
            Gracias {nombre}, he recibido tu mensaje.
            
            📧 Pronto me pondré en contacto a: {email}
            
            **(Nota: Este es un formulario de demostración)**
            """)
        else:
            st.error("❌ Por favor completa todos los campos")

st.divider()

st.markdown("## 🔗 Enlaces Rápidos")

button_col1, button_col2, button_col3 = st.columns(3)

with button_col1:
    st.markdown(f"""
    <a href="mailto:{DATOS_PERSONALES['CORREO']}" style="text-decoration: none;">
        <button style="width: 100%; padding: 0.75rem; background: #0891b2; color: white; border: none; border-radius: 8px; font-weight: 600; cursor: pointer;">
            📧 Enviar Email
        </button>
    </a>
    """, unsafe_allow_html=True)

with button_col2:
    st.markdown(f"""
    <a href="https://linkedin.com/in/alexiburgos" target="_blank" style="text-decoration: none;">
        <button style="width: 100%; padding: 0.75rem; background: #0891b2; color: white; border: none; border-radius: 8px; font-weight: 600; cursor: pointer;">
            💼 LinkedIn
        </button>
    </a>
    """, unsafe_allow_html=True)

with button_col3:
    st.markdown(f"""
    <a href="tel:{DATOS_PERSONALES['TELEFONO']}" style="text-decoration: none;">
        <button style="width: 100%; padding: 0.75rem; background: #0891b2; color: white; border: none; border-radius: 8px; font-weight: 600; cursor: pointer;">
            📞 Llamar
        </button>
    </a>
    """, unsafe_allow_html=True)

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
