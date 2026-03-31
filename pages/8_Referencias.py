# pages/8_Referencias.py
# -*- coding: utf-8 -*-
import streamlit as st

from shared.cv_content import REFERENCIAS
from shared.ui_components import render_page_header

st.set_page_config(page_title="Referencias - Alexi Burgos CV", page_icon="👥", layout="wide")

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

.referencia-card {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    margin: 1.5rem 0;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #0891b2;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    transition: all 0.3s ease;
}

.referencia-card:hover {
    box-shadow: 0 8px 20px rgba(8,145,178,0.15);
    transform: translateY(-2px);
}

.ref-nombre {
    font-size: 1.25rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 0.5rem;
}

.ref-cargo {
    color: #0891b2;
    font-weight: 600;
    font-size: 0.95rem;
    margin-bottom: 0.25rem;
}

.ref-organizacion {
    color: #64748b;
    font-size: 0.9rem;
    margin-bottom: 1rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #e2e8f0;
}

.ref-relacion {
    color: #475569;
    font-size: 0.9rem;
    font-style: italic;
    margin-bottom: 1rem;
    background: #f8fafc;
    padding: 0.75rem;
    border-radius: 6px;
    border-left: 3px solid #059669;
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
    color: #0891b2;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

header_gradient = "linear-gradient(135deg, #64748b 0%, #94a3b8 100%)"
render_page_header(
    "👥 Referencias Profesionales",
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
                <span style="color: #0891b2;">{ref['telefono']}</span>
            </div>
            <div class="ref-item">
                <span class="ref-icon">📧</span>
                <span style="color: #0891b2;">{ref['email']}</span>
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
