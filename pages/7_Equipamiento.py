# pages/7_Equipamiento.py
# -*- coding: utf-8 -*-
import streamlit as st

from shared.cv_content import EQUIPAMIENTO, INTERESES
from shared.ui_components import EXECUTIVE_HEADER_GRADIENT, render_page_header

st.set_page_config(page_title="Equipamiento - Alexi Burgos CV", page_icon="💻", layout="wide")

# CSS
st.markdown("""
<style>
.equipo-card {
    background: #FFFFFF;
    padding: 1.4rem;
    border-radius: 12px;
    margin: 0.9rem 0;
    border: 1px solid #CBD5E1;
    border-left: 4px solid #0E7490;
    box-shadow: 0 8px 20px rgba(15, 23, 42, 0.07);
}

.equipo-titulo {
    font-size: 1.08rem;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 0.7rem;
}

.equipo-contenido {
    color: #475569;
    font-size: 0.95rem;
    line-height: 1.6;
}

.intereses-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin: 2rem 0;
}

.interes-badge {
    background: #FFFFFF;
    color: #0F172A;
    padding: 0.92rem;
    border-radius: 10px;
    text-align: center;
    font-weight: 600;
    border: 1px solid #CBD5E1;
    box-shadow: 0 6px 16px rgba(15, 23, 42, 0.07);
    transition: all 0.3s ease;
}

.interes-badge:hover {
    transform: translateY(-1px);
    border-color: #0E7490;
    box-shadow: 0 10px 20px rgba(14, 116, 144, 0.14);
}
</style>
""", unsafe_allow_html=True)

header_gradient = EXECUTIVE_HEADER_GRADIENT
render_page_header(
    "Equipamiento e Intereses",
    "Recursos y áreas de interés personal",
    header_gradient,
)

st.markdown("## 🖥️ Equipamiento para Trabajo Remoto/Híbrido")

for categoria, descripcion in EQUIPAMIENTO.items():
    st.markdown(f"""
    <div class="equipo-card">
        <div class="equipo-titulo">🔹 {categoria}</div>
        <div class="equipo-contenido">{descripcion}</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown("## 🎯 Intereses Personales")

cols = st.columns(4)
for i, interes in enumerate(INTERESES):
    with cols[i % 4]:
        emoji_map = {
            "Gestión Educacional": "🎓",
            "Producción y Edición Musical": "🎵",
            "Viajes": "✈️",
            "Fotografía": "📸",
            "Ciencia": "🔬",
            "Tecnología": "⚙️",
            "Ajedrez": "♟️",
            "Voleibol": "🏐",
        }
        emoji = emoji_map.get(interes, "✨")
        st.markdown(f"""
        <div class="interes-badge">{emoji} {interes}</div>
        """, unsafe_allow_html=True)

st.divider()

st.markdown("""
### 💡 Lo que Esto Significa

Mis intereses reflejan una combinación de:

- **Educación:** Pasión por la gestión educacional y desarrollo profesional continuo
- **Creatividad:** Producción musical y fotografía como expresión artística
- **Bienestar:** Deportes (voleibol) y juegos estratégicos (ajedrez) para equilibrio mental
- **Exploración:** Viajes y ciencia como búsqueda constante de conocimiento
- **Innovación:** Tecnología como herramienta transformadora
""")
