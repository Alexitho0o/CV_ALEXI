# pages/8_Referencias.py
# -*- coding: utf-8 -*-
import streamlit as st

from shared.cv_content import REFERENCIAS
from shared.ui_components import EXECUTIVE_HEADER_GRADIENT, render_page_header

st.set_page_config(page_title="Referencias - Alexi Burgos CV", page_icon="👥", layout="wide")

# CSS
st.markdown("""
<style>
.referencia-card {
    background: #FFFFFF;
    padding: 1.45rem;
    border-radius: 12px;
    margin: 1rem 0;
    border: 1px solid #CBD5E1;
    border-left: 4px solid #0E7490;
    box-shadow: 0 8px 20px rgba(15, 23, 42, 0.07);
    transition: all 0.3s ease;
}

.referencia-card:hover {
    box-shadow: 0 12px 24px rgba(14, 116, 144, 0.14);
    transform: translateY(-1px);
}

.ref-nombre {
    font-size: 1.08rem;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 0.35rem;
}

.ref-cargo {
    color: #0E7490;
    font-weight: 600;
    font-size: 0.92rem;
    margin-bottom: 0.25rem;
}

.ref-organizacion {
    color: #475569;
    font-size: 0.88rem;
    margin-bottom: 1rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #CBD5E1;
}

.ref-relacion {
    color: #475569;
    font-size: 0.9rem;
    font-style: italic;
    margin-bottom: 1rem;
    background: #F8FAFC;
    padding: 0.75rem;
    border-radius: 6px;
    border-left: 3px solid #1E3A8A;
}

.ref-contacto {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.ref-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: #475569;
    font-size: 0.9rem;
}

.ref-icon {
    color: #0E7490;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

header_gradient = EXECUTIVE_HEADER_GRADIENT
render_page_header(
    "Referencias Profesionales",
    "Personas que pueden validar mi experiencia y desempeño",
    header_gradient,
)

st.markdown("## Contactos de Referencia")

for ref in REFERENCIAS:
    st.markdown(f"""
    <div class="referencia-card">
        <div class="ref-nombre">👤 {ref['nombre']}</div>
        <div class="ref-cargo">{ref['cargo']}</div>
        <div class="ref-organizacion">🏢 {ref['organizacion']}</div>
        <div class="ref-relacion">💼 {ref['relacion']}</div>
        <div class="ref-contacto">
            <div class="ref-item">
                <span class="ref-icon">📱</span>
                <span style="color: #0E7490;">{ref['telefono']}</span>
            </div>
            <div class="ref-item">
                <span class="ref-icon">📧</span>
                <span style="color: #0E7490;">{ref['email']}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown("""
### 📋 Nota Importante

Estas referencias pueden confirmar:

- **Desempeño profesional:** Calidad de trabajo, responsabilidad y cumplimiento
- **Habilidades técnicas:** Proficiencia en herramientas y plataformas utilizadas
- **Competencias blandas:** Liderazgo, comunicación, resolución de conflictos
- **Experiencia académica:** Diseño curricular, evaluación y gestión educativa
- **Logros específicos:** Proyectos exitosos y métricas de mejora

Algunos han sido mis supervisores directos; otros, colegas de trabajo. 
Todos pueden atestiguar mi profesionalismo y compromiso con la excelencia.
""")
