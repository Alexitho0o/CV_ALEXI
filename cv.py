# cv.py - Home Page
# -*- coding: utf-8 -*-
from typing import Any, Dict, List, Tuple

import streamlit as st

from shared.cv_content import DATOS_PERSONALES
from shared.ui_components import (
    EXECUTIVE_HEADER_GRADIENT,
    inject_sidebar_navigation_styles,
    render_quick_links,
)

st.set_page_config(page_title="Alexi Burgos CV", page_icon="📄", layout="wide")
inject_sidebar_navigation_styles()

# gradient for main page header (slate-teal executive style)
header_gradient = EXECUTIVE_HEADER_GRADIENT

PALETA_GRUPOS = {
    "Data & Business Intelligence": "#0E7490",
    "Plataformas Educativas": "#1E3A8A",
    "Herramientas Ofimáticas y Colaboración": "#475569",
    "Sistemas Operativos y Dispositivos": "#475569",
    "Idiomas": "#475569",
    "Creatividad": "#475569",
}

# CSS Global
def inyectar_css() -> None:
    st.markdown(
        """
        <style>
        .home-hero-meta {
            color: #CBD5E1;
            font-size: 0.97rem;
            margin: 0.3rem 0;
            font-weight: 500;
        }

        .hero-title {
            color: #F8FAFC;
            font-size: 1rem;
            margin-top: 0.95rem;
            background: rgba(255, 255, 255, 0.14);
            border: 1px solid rgba(226, 232, 240, 0.35);
            padding: 0.85rem 1.1rem;
            border-radius: 10px;
            display: inline-block;
            line-height: 1.5;
            max-width: 960px;
        }

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.85rem;
            margin: 1rem 0 1.35rem;
        }

        .skill-tile {
            background: #FFFFFF;
            border: 1px solid #CBD5E1;
            border-top: 4px solid var(--tile-accent);
            border-radius: 12px;
            padding: 1rem;
            min-height: 120px;
            box-shadow: 0 8px 22px rgba(15, 23, 42, 0.06);
        }

        .skill-tile h3 {
            margin: 0 0 0.45rem 0;
            font-size: 1.02rem;
            color: #0F172A;
            font-weight: 750;
        }

        .skill-tile p {
            margin: 0;
            color: #475569;
            font-size: 0.94rem;
            font-weight: 520;
            line-height: 1.55;
        }

        .specialization-card {
            background: #FFFFFF;
            border: 1px solid #CBD5E1;
            border-radius: 12px;
            padding: 1rem 1.1rem;
            box-shadow: 0 8px 20px rgba(15, 23, 42, 0.06);
        }

        .specialization-card {
            border-left: 4px solid #0E7490;
            margin: 0.8rem 0 1rem;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

inyectar_css()

# Dashboard mejorado de habilidades con visualización por categoría
def construir_dashboard_habilidades(
    habilidades: List[Tuple[str, List[Tuple[str, int]]]],
    alto_px: int = 600,
    ancho_px: int = 900,
    dpi: int = 150,
) -> 'Any':
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import pandas as pd
    
    filas: List[Dict[str, Any]] = []
    for grupo, items in habilidades:
        for (habilidad, pct) in items:
            filas.append({"grupo": grupo, "habilidad": habilidad, "pct": int(pct)})

    df = pd.DataFrame(filas)
    if df.empty:
        df = pd.DataFrame([{"grupo": "Sin datos", "habilidad": "Sin habilidades", "pct": 0}])

    df["grupo"] = df["grupo"].astype(str)
    df["habilidad"] = df["habilidad"].astype(str)
    df["pct"] = pd.to_numeric(df["pct"], errors="coerce").fillna(0).clip(0, 100).astype(int)

    orden_grupo: List[str] = [g for g, _ in habilidades] or sorted(df["grupo"].unique().tolist())
    df["grupo"] = pd.Categorical(df["grupo"], categories=orden_grupo, ordered=True)
    df = df.sort_values(["grupo", "pct"], ascending=[True, False]).reset_index(drop=True)

    n = len(df)
    fig_w = ancho_px / dpi
    fig_h = alto_px / dpi

    plt.close("all")
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=dpi)

    y = list(range(n))[::-1]
    colores = [PALETA_GRUPOS.get(g, "#0E7490") for g in df["grupo"].tolist()][::-1]
    valores = df["pct"].tolist()[::-1]
    etiquetas = df["habilidad"].tolist()[::-1]
    grupos_plot = df["grupo"].tolist()[::-1]

    # Fondo
    ax.barh(y, [100] * n, color="#F1F5F9", edgecolor="none", height=0.65)
    # Barras principales con gradiente visual
    ax.barh(y, valores, color=colores, edgecolor="none", height=0.65, alpha=0.9)

    ax.set_xlim(0, 105)
    ax.set_yticks(y)
    ax.set_yticklabels(etiquetas, fontsize=10, fontweight="600", color="#0F172A")
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.tick_params(axis="x", labelsize=9, colors="#475569", length=3)
    
    # Estilos de spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(1)
    ax.spines["bottom"].set_linewidth(1)
    ax.spines["left"].set_color("#CBD5E1")
    ax.spines["bottom"].set_color("#CBD5E1")
    
    # Grid mejorado
    ax.grid(axis="x", linestyle="--", linewidth=0.5, alpha=0.4, color="#CBD5E1")
    ax.set_axisbelow(True)

    # Etiquetas de porcentaje
    for i, v in enumerate(valores):
        if v >= 50:
            ax.text(v - 3, y[i], f"{v}%", va="center", ha="right", fontsize=9, 
                   color="white", fontweight="700")
        else:
            ax.text(min(v + 2, 101), y[i], f"{v}%", va="center", ha="left", fontsize=9, 
                   color="#0F172A", fontweight="700")

    # Separadores entre categorías
    for i in range(1, n):
        if grupos_plot[i] != grupos_plot[i - 1]:
            ax.axhline(y=y[i] - 0.5, color="#CBD5E1", linewidth=2, linestyle="-", alpha=0.3)

    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")
    fig.tight_layout()
    return fig

# Página Principal (Home)
st.markdown(
    f"""
    <div class="app-hero" style="background: {header_gradient};">
        <h1>{DATOS_PERSONALES['NOMBRE']}</h1>
        <div class="home-hero-meta">📍 {DATOS_PERSONALES['UBICACION']} | 📱 {DATOS_PERSONALES['TELEFONO']}</div>
        <div class="home-hero-meta">📧 {DATOS_PERSONALES['CORREO']} | 💼 {DATOS_PERSONALES['LINKEDIN']}</div>
        <div class="hero-title">{DATOS_PERSONALES['TITULO']}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("## 📋 Resumen Profesional")
st.write(DATOS_PERSONALES["RESUMEN"])

metric_col1, metric_col2, metric_col3 = st.columns(3)
with metric_col1:
    st.metric("Trayectoria en Logística", "+13 años")
with metric_col2:
    st.metric("Trayectoria en Educación", "+6 años")
with metric_col3:
    st.metric("Posiciones Registradas", "10")

st.divider()

st.markdown("## 📌 Destrezas Clave")

skills_html = """
<div class="skills-grid">
    <div class="skill-tile" style="--tile-accent:#0E7490;">
        <h3>📊 Análisis de Datos</h3>
        <p>Power BI, Excel avanzado y Python orientado a decisiones.</p>
    </div>
    <div class="skill-tile" style="--tile-accent:#1E3A8A;">
        <h3>🏫 Plataformas Educativas</h3>
        <p>Gestión y operación académica en Banner, Moodle y Blackboard.</p>
    </div>
    <div class="skill-tile" style="--tile-accent:#475569;">
        <h3>🔧 Ofimática y Colaboración</h3>
        <p>Office 365, Google Workspace y herramientas de evaluación activa.</p>
    </div>
    <div class="skill-tile" style="--tile-accent:#475569;">
        <h3>💻 Sistemas y Dispositivos</h3>
        <p>MacOS, Windows, iOS y Android para soporte de entornos mixtos.</p>
    </div>
    <div class="skill-tile" style="--tile-accent:#475569;">
        <h3>🌐 Idiomas</h3>
        <p>Español nativo e inglés técnico aplicado a documentación y datos.</p>
    </div>
    <div class="skill-tile" style="--tile-accent:#475569;">
        <h3>🎓 Especialización</h3>
        <p>Logística, analítica institucional, docencia y mejora continua.</p>
    </div>
</div>
"""

st.markdown(skills_html, unsafe_allow_html=True)

st.divider()

st.markdown("## 🎯 Especialización")
st.markdown(
    """
    <div class="specialization-card">
        <ul>
            <li><strong>Análisis Institucional:</strong> construcción de indicadores y tableros para gestión académica.</li>
            <li><strong>Gestión Académica:</strong> coordinación, acreditación y mejora continua en educación superior.</li>
            <li><strong>Business Intelligence:</strong> reporte estratégico y seguimiento KPI/OKR para toma de decisiones.</li>
            <li><strong>Docencia Aplicada:</strong> logística, compras estratégicas y gestión de operaciones.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()
st.markdown("## 🔗 Enlaces Rápidos")
render_quick_links(
    DATOS_PERSONALES["CORREO"],
    DATOS_PERSONALES["TELEFONO"],
    "https://linkedin.com/in/alexiburgos",
)

st.markdown("## Explora Mis Secciones")
nav_items = [
    ("pages/2_Experiencia.py", "Experiencia", "💼", "Trayectoria profesional cronológica y por área."),
    ("pages/3_Habilidades.py", "Habilidades", "🧠", "Competencias técnicas y herramientas clave."),
    ("pages/4_Educacion.py", "Educación", "🎓", "Títulos profesionales y formación de postítulo."),
    ("pages/6_Competencias.py", "Competencias", "📘", "Fortalezas metodológicas y de gestión."),
    ("pages/7_Equipamiento.py", "Equipamiento", "💻", "Recursos de trabajo remoto e intereses."),
    ("pages/8_Referencias.py", "Referencias", "👥", "Validación profesional de desempeño."),
    ("pages/5_Contacto.py", "Contacto", "📧", "Canales directos para oportunidades y proyectos."),
]

for i in range(0, len(nav_items), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(nav_items):
            path, label, icon, descripcion = nav_items[i + j]
            with col:
                st.page_link(path, label=label, icon=icon, use_container_width=True)
                st.caption(descripcion)
