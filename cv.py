# cv.py - Home Page
# -*- coding: utf-8 -*-
from typing import Any, Dict, List, Tuple

import streamlit as st

from shared.cv_content import DATOS_PERSONALES
from shared.ui_components import render_quick_links

st.set_page_config(page_title="Alexi Burgos CV", page_icon="📄", layout="wide")

# gradient for main page header (mirrors section style in other pages)
header_gradient = "linear-gradient(135deg, #0891b2 0%, #06b6d4 100%)"

PALETA_GRUPOS = {
    "Data & Business Intelligence": "#0891b2",
    "Plataformas Educativas": "#7c3aed",
    "Herramientas Ofimáticas y Colaboración": "#059669",
    "Sistemas Operativos y Dispositivos": "#f59e0b",
    "Idiomas": "#ef4444",
    "Creatividad": "#ec4899",
}

# CSS Global
def inyectar_css() -> None:
    # global styles (hero-header now matches primary gradient)
    st.markdown("""
        <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); }
        
        .hero-header {
            background: """ + header_gradient + """;
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
            letter-spacing: -0.02em;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        
        .hero-sub {
            color: #cbd5e1;
            font-size: 1rem;
            margin: 0.5rem 0;
            font-weight: 500;
        }
        
        .hero-title {
            color: white;
            font-weight: 600;
            font-size: 1rem;
            margin-top: 1rem;
            background: rgba(255, 255, 255, 0.15);
            padding: 1rem 1.25rem;
            border-radius: 8px;
            display: inline-block;
            line-height: 1.5;
        }
        
        .section-card {
            background: white;
            padding: 2.5rem;
            border-radius: 14px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            margin: 2rem 0;
        }
        
        .card-header {
            display: flex;
            align-items: center;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 3px solid #0891b2;
        }
        
        .card-header h2 {
            font-size: 1.8rem;
            color: #0f172a;
            font-weight: 900;
            margin: 0;
        }
        
        .experience-item {
            margin: 1.5rem 0;
            padding: 1.5rem;
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            border-left: 4px solid #0891b2;
            border-radius: 8px;
        }
        
        .role {
            font-weight: 800;
            color: #0f172a;
            font-size: 1.1rem;
            margin-bottom: 0.3rem;
        }
        
        .org {
            color: #64748b;
            font-size: 0.95rem;
            margin-bottom: 0.5rem;
        }
        
        .dates {
            color: #0891b2;
            font-weight: 600;
            font-size: 0.9rem;
        }
        
        .bullets {
            margin-top: 0.8rem;
            padding-left: 1.5rem;
        }
        
        .bullets li {
            margin-bottom: 0.5rem;
            color: #334155;
            font-size: 0.95rem;
            line-height: 1.6;
        }
        
        .skill-category {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
            border-left: 4px solid #0891b2;
        }
        
        .skill-category.data { border-left-color: #0891b2; }
        .skill-category.academic { border-left-color: #059669; }
        .skill-category.platforms { border-left-color: #7c3aed; }
        
        .education-item {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
            border: 1px solid #e2e8f0;
            border-top: 4px solid #0891b2;
        }
        
        .degree {
            font-weight: 700;
            color: #0f172a;
            font-size: 1.05rem;
            margin-bottom: 0.3rem;
        }
        
        .institution {
            color: #64748b;
            font-size: 0.95rem;
            margin-bottom: 0.3rem;
        }
        
        .year {
            color: #0891b2;
            font-weight: 600;
            font-size: 0.9rem;
        }
        </style>
    """, unsafe_allow_html=True)

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
    colores = [PALETA_GRUPOS.get(g, "#2E5EAA") for g in df["grupo"].tolist()][::-1]
    valores = df["pct"].tolist()[::-1]
    etiquetas = df["habilidad"].tolist()[::-1]
    grupos_plot = df["grupo"].tolist()[::-1]

    # Fondo
    ax.barh(y, [100] * n, color="#f1f5f9", edgecolor="none", height=0.65)
    # Barras principales con gradiente visual
    ax.barh(y, valores, color=colores, edgecolor="none", height=0.65, alpha=0.9)

    ax.set_xlim(0, 105)
    ax.set_yticks(y)
    ax.set_yticklabels(etiquetas, fontsize=10, fontweight="600", color="#1e293b")
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.tick_params(axis="x", labelsize=9, colors="#64748b", length=3)
    
    # Estilos de spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(1)
    ax.spines["bottom"].set_linewidth(1)
    ax.spines["left"].set_color("#cbd5e1")
    ax.spines["bottom"].set_color("#cbd5e1")
    
    # Grid mejorado
    ax.grid(axis="x", linestyle="--", linewidth=0.5, alpha=0.4, color="#cbd5e1")
    ax.set_axisbelow(True)

    # Etiquetas de porcentaje
    for i, v in enumerate(valores):
        if v >= 50:
            ax.text(v - 3, y[i], f"{v}%", va="center", ha="right", fontsize=9, 
                   color="white", fontweight="700")
        else:
            ax.text(min(v + 2, 101), y[i], f"{v}%", va="center", ha="left", fontsize=9, 
                   color="#0f172a", fontweight="700")

    # Separadores entre categorías
    for i in range(1, n):
        if grupos_plot[i] != grupos_plot[i - 1]:
            ax.axhline(y=y[i] - 0.5, color="#cbd5e1", linewidth=2, linestyle="-", alpha=0.3)

    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")
    fig.tight_layout()
    return fig

# Página Principal (Home)
# header uses the same gradient style as other pages
st.markdown(f"""
<div style="background: {header_gradient}; color: white; padding: 3rem 2rem; border-radius: 16px; margin-bottom: 2rem; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
    <h1>🎯 {DATOS_PERSONALES['NOMBRE']}</h1>
    <div class="page-sub">📍 {DATOS_PERSONALES['UBICACION']} | 📱 {DATOS_PERSONALES['TELEFONO']}</div>
    <div class="page-sub">📧 {DATOS_PERSONALES['CORREO']} | 💼 {DATOS_PERSONALES['LINKEDIN']}</div>
    <div class="hero-title">{DATOS_PERSONALES['TITULO']}</div>
</div>
""", unsafe_allow_html=True)

st.markdown("## 📋 Resumen Profesional")
st.write(DATOS_PERSONALES["RESUMEN"])

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

st.divider()
# Quick links also on home page
st.markdown("## 🔗 Enlaces Rápidos")
render_quick_links(
    DATOS_PERSONALES["CORREO"],
    DATOS_PERSONALES["TELEFONO"],
    "https://linkedin.com/in/alexiburgos",
)

st.markdown("## 🚀 Explora mis secciones en el menú lateral →")

col1, col2, col3 = st.columns(3)
with col1:
    st.info("**💼 Experiencia**\nHistorial laboral completo")
with col2:
    st.info("**🎯 Habilidades**\nCompetencias profesionales")
with col3:
    st.info("**🎓 Educación**\nFormación académica")

col1, col2, col3 = st.columns(3)
with col1:
    st.info("**🎯 Competencias**\nÁreas de especialización")
with col2:
    st.info("**💻 Equipamiento**\nRecursos e intereses")
with col3:
    st.info("**👥 Referencias**\nContactos profesionales")

col1, col2 = st.columns(2)
with col1:
    st.info("**📧 Contacto**\nCómo ponerse en contacto")
