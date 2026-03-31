# pages/7_Equipamiento.py
# -*- coding: utf-8 -*-
import streamlit as st

from shared.cv_content import EQUIPAMIENTO, INTERESES
from shared.ui_components import render_page_header

st.set_page_config(page_title="Equipamiento - Alexi Burgos CV", page_icon="💻", layout="wide")

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

.equipo-card {
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    padding: 2rem;
    border-radius: 12px;
    margin: 1.5rem 0;
    border-left: 4px solid #0891b2;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.equipo-titulo {
    font-size: 1.3rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 1rem;
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
    background: linear-gradient(135deg, #0891b2 0%, #0284c7 100%);
    color: white;
    padding: 1rem;
    border-radius: 10px;
    text-align: center;
    font-weight: 600;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
}

.interes-badge:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

header_gradient = "linear-gradient(135deg, #0891b2 0%, #06b6d4 100%)"
render_page_header(
    "💻 Equipamiento e Intereses",
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
