# pages/3_Habilidades.py
# -*- coding: utf-8 -*-
import streamlit as st
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import Any, Dict, List, Tuple

st.set_page_config(page_title="Habilidades - Alexi Burgos CV", page_icon="🎯", layout="wide")

HABILIDADES: List[Tuple[str, List[Tuple[str, int]]]] = [
    ("Data & Business Intelligence", [
        ("Power BI (dashboards KPI/OKR)", 90),
        ("Excel avanzado (modelamiento/visualización)", 95),
        ("Python (análisis de datos)", 75),
    ]),
    ("Plataformas Educativas", [
        ("Banner", 80),
        ("Blackboard", 75),
        ("Moodle (intermedio)", 75),
        ("Bettersoft U+", 70),
        ("Syllabus", 70),
    ]),
    ("Herramientas Ofimáticas y Colaboración", [
        ("MS Office 365 (Word, Excel, PowerPoint)", 95),
        ("GSuite (Gmail, Docs, Sheets, Meet)", 90),
        ("Kahoot (evaluación gamificada)", 85),
        ("Mentimeter (encuestas interactivas)", 85),
    ]),
    ("Sistemas Operativos y Dispositivos", [
        ("MacOS", 95),
        ("Windows", 90),
        ("iOS", 90),
        ("Android (intermedio)", 75),
    ]),
    ("Idiomas", [
        ("Inglés técnico (lectora/comprensión)", 80),
        ("Español (nativo)", 100),
    ]),
    ("Creatividad", [
        ("Autor y Compositor", 85),
        ("Producción Musical", 80),
        ("Edición Musical", 75),
    ]),
]

PALETA_GRUPOS = {
    "Data & Business Intelligence": "#0891b2",
    "Plataformas Educativas": "#7c3aed",
    "Herramientas Ofimáticas y Colaboración": "#059669",
    "Sistemas Operativos y Dispositivos": "#f59e0b",
    "Idiomas": "#ef4444",
    "Creatividad": "#ec4899",
}

def grafico_barh_simple(grupo: str, items: List[Tuple[str, int]], color: str, height_px: int = 300) -> Any:
    """Gráfico horizontal para Data & BI"""
    skills = [s for s, _ in items]
    niveles = [n for _, n in items]
    
    fig, ax = plt.subplots(figsize=(8, height_px/100), dpi=100)
    y_pos = np.arange(len(skills))
    
    ax.barh(y_pos, niveles, color=color, alpha=0.8, edgecolor='white', linewidth=2)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(skills, fontsize=10, fontweight='500')
    ax.set_xlabel('Nivel %', fontsize=10, fontweight='600', color='#64748b')
    ax.set_xlim(0, 105)
    ax.invert_yaxis()
    
    # Etiquetas en las barras
    for i, v in enumerate(niveles):
        ax.text(v - 2, i, f'{v}%', va='center', ha='right', color='white', fontweight='700', fontsize=9)
    
    ax.grid(axis='x', alpha=0.2, linestyle='--')
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#e2e8f0')
    ax.spines['bottom'].set_color('#e2e8f0')
    
    fig.patch.set_facecolor('white')
    plt.tight_layout()
    return fig

def grafico_donut(grupo: str, items: List[Tuple[str, int]], color: str, height_px: int = 300) -> Any:
    """Gráfico tipo donut para Plataformas Educativas"""
    skills = [s.replace(' (', '\n(') for s, _ in items]
    niveles = [n for _, n in items]
    
    fig, ax = plt.subplots(figsize=(7, height_px/100), dpi=100)
    
    colors_gradient = plt.cm.Blues(np.linspace(0.4, 0.9, len(niveles)))
    wedges, texts, autotexts = ax.pie(
        niveles, labels=skills, autopct='%1.0f%%',
        colors=colors_gradient, startangle=90,
        textprops={'fontsize': 9, 'weight': '600', 'color': '#334155'},
        wedgeprops=dict(edgecolor='white', linewidth=2)
    )
    
    # Hacer el donut
    centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='#e2e8f0', linewidth=2)
    ax.add_artist(centre_circle)
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('700')
        autotext.set_fontsize(9)
    
    fig.patch.set_facecolor('white')
    plt.tight_layout()
    return fig

def grafico_barras_verticales(grupo: str, items: List[Tuple[str, int]], color: str, height_px: int = 300) -> Any:
    """Gráfico de barras verticales para Herramientas"""
    skills = [s.replace(' (', '\n(') for s, _ in items]
    niveles = [n for _, n in items]
    
    fig, ax = plt.subplots(figsize=(9, height_px/100), dpi=100)
    x_pos = np.arange(len(skills))
    
    ax.bar(x_pos, niveles, color=color, alpha=0.8, edgecolor='white', linewidth=2, width=0.6)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(skills, fontsize=9, fontweight='500', rotation=45, ha='right')
    ax.set_ylabel('Nivel %', fontsize=10, fontweight='600', color='#64748b')
    ax.set_ylim(0, 105)
    
    # Etiquetas en las barras
    for i, v in enumerate(niveles):
        ax.text(i, v + 2, f'{v}%', ha='center', va='bottom', fontweight='700', fontsize=9, color='#0f172a')
    
    ax.grid(axis='y', alpha=0.2, linestyle='--')
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#e2e8f0')
    ax.spines['bottom'].set_color('#e2e8f0')
    
    fig.patch.set_facecolor('white')
    plt.tight_layout()
    return fig

def grafico_circular(grupo: str, items: List[Tuple[str, int]], color: str, height_px: int = 300) -> Any:
    """Gráfico circular para Sistemas Operativos"""
    skills = [s for s, _ in items]
    niveles = [n for _, n in items]
    
    fig, ax = plt.subplots(figsize=(7, height_px/100), dpi=100)
    
    colors_gradient = plt.cm.Oranges(np.linspace(0.4, 0.9, len(niveles)))
    wedges, texts, autotexts = ax.pie(
        niveles, labels=skills, autopct='%1.0f%%',
        colors=colors_gradient, startangle=45,
        textprops={'fontsize': 9, 'weight': '600', 'color': '#334155'},
        wedgeprops=dict(edgecolor='white', linewidth=2)
    )
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('700')
        autotext.set_fontsize(9)
    
    fig.patch.set_facecolor('white')
    plt.tight_layout()
    return fig

def grafico_barras_idiomas(grupo: str, items: List[Tuple[str, int]], color: str, height_px: int = 300) -> Any:
    """Gráfico horizontal para Idiomas"""
    skills = [s for s, _ in items]
    niveles = [n for _, n in items]
    
    fig, ax = plt.subplots(figsize=(7, height_px/100), dpi=100)
    y_pos = np.arange(len(skills))
    
    ax.barh(y_pos, niveles, color=color, alpha=0.8, edgecolor='white', linewidth=2)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(skills, fontsize=10, fontweight='500')
    ax.set_xlabel('Nivel %', fontsize=10, fontweight='600', color='#64748b')
    ax.set_xlim(0, 105)
    ax.invert_yaxis()
    
    for i, v in enumerate(niveles):
        ax.text(v - 2, i, f'{v}%', va='center', ha='right', color='white', fontweight='700', fontsize=9)
    
    ax.grid(axis='x', alpha=0.2, linestyle='--')
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#e2e8f0')
    ax.spines['bottom'].set_color('#e2e8f0')
    
    fig.patch.set_facecolor('white')
    plt.tight_layout()
    return fig

def grafico_radar(grupo: str, items: List[Tuple[str, int]], color: str, height_px: int = 300) -> Any:
    """Gráfico radar para Creatividad"""
    skills = [s for s, _ in items]
    niveles = [n for _, n in items]
    
    # Número de variables
    num_vars = len(skills)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    niveles += niveles[:1]  # Completar el ciclo
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(7, height_px/100), dpi=100, subplot_kw=dict(projection='polar'))
    
    ax.plot(angles, niveles, 'o-', linewidth=2, color=color, label='Nivel')
    ax.fill(angles, niveles, alpha=0.25, color=color)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(skills, fontsize=9, fontweight='500')
    ax.set_ylim(0, 100)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], fontsize=8, color='#64748b')
    ax.grid(True, color='#e2e8f0', alpha=0.5)
    
    fig.patch.set_facecolor('white')
    plt.tight_layout()
    return fig

def construir_dashboard_habilidades(habilidades, alto_px=700, ancho_px=1200, dpi=150):
    filas = []
    for grupo, items in habilidades:
        for (habilidad, pct) in items:
            filas.append({"grupo": grupo, "habilidad": habilidad, "pct": int(pct)})

    df = pd.DataFrame(filas)
    if df.empty:
        df = pd.DataFrame([{"grupo": "Sin datos", "habilidad": "Sin habilidades", "pct": 0}])

    df["grupo"] = df["grupo"].astype(str)
    df["habilidad"] = df["habilidad"].astype(str)
    df["pct"] = pd.to_numeric(df["pct"], errors="coerce").fillna(0).clip(0, 100).astype(int)

    orden_grupo = [g for g, _ in habilidades] or sorted(df["grupo"].unique().tolist())
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

    # Fondo gris
    ax.barh(y, [100] * n, color="#f1f5f9", edgecolor="none", height=0.65)
    # Barras de color
    ax.barh(y, valores, color=colores, edgecolor="none", height=0.65, alpha=0.9)

    ax.set_xlim(0, 105)
    ax.set_yticks(y)
    ax.set_yticklabels(etiquetas, fontsize=11, fontweight="600", color="#1e293b")
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.tick_params(axis="x", labelsize=10, colors="#64748b", length=3)
    
    # Estilos mejorados
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(1.5)
    ax.spines["bottom"].set_linewidth(1.5)
    ax.spines["left"].set_color("#cbd5e1")
    ax.spines["bottom"].set_color("#cbd5e1")
    
    ax.grid(axis="x", linestyle="--", linewidth=0.5, alpha=0.4, color="#cbd5e1")
    ax.set_axisbelow(True)

    # Etiquetas con mejor contraste
    for i, v in enumerate(valores):
        if v >= 50:
            ax.text(v - 3, y[i], f"{v}%", va="center", ha="right", fontsize=10, 
                   color="white", fontweight="700")
        else:
            ax.text(min(v + 2, 101), y[i], f"{v}%", va="center", ha="left", fontsize=10, 
                   color="#0f172a", fontweight="700")

    # Separadores entre categorías
    for i in range(1, n):
        if grupos_plot[i] != grupos_plot[i - 1]:
            ax.axhline(y=y[i] - 0.5, color="#cbd5e1", linewidth=2.5, linestyle="-", alpha=0.3)

    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")
    fig.tight_layout()
    return fig

# CSS
st.markdown("""
<style>
.skill-category {
    background: linear-gradient(135deg, #f8fafc 0%, white 100%);
    padding: 1.5rem;
    border-radius: 12px;
    margin: 1rem 0;
    border-left: 5px solid #0891b2;
}
.skill-category h3 {
    margin: 0 0 1rem 0;
    color: #0f172a;
    font-size: 1.2rem;
}
.skill-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.8rem 0;
    border-bottom: 1px solid #e2e8f0;
}
.skill-item:last-child {
    border-bottom: none;
}
.skill-name {
    flex: 1;
    color: #334155;
    font-weight: 500;
}
.skill-level {
    text-align: right;
    font-weight: 700;
    color: #0891b2;
}
</style>
""", unsafe_allow_html=True)

st.markdown("# 🎯 Habilidades y Competencias")

st.markdown("*Especialista en análisis de datos, gestión académica y educación*")

# Gráfico principal
st.markdown("## 📊 Vista General de Competencias")
fig = construir_dashboard_habilidades(HABILIDADES, alto_px=700, ancho_px=1200, dpi=150)
st.pyplot(fig, clear_figure=True, width='stretch')

st.divider()

st.divider()

# Detalles por categoría con gráficos variados
st.markdown("## 📋 Detalle por Área")

# Mapeo de funciones de gráficos
graficos_por_grupo = {
    "Data & Business Intelligence": (grafico_barh_simple, "#0891b2"),
    "Plataformas Educativas": (grafico_donut, "#7c3aed"),
    "Herramientas Ofimáticas y Colaboración": (grafico_barras_verticales, "#059669"),
    "Sistemas Operativos y Dispositivos": (grafico_circular, "#f59e0b"),
    "Idiomas": (grafico_barras_idiomas, "#ef4444"),
    "Creatividad": (grafico_radar, "#ec4899"),
}

# Mostrar cada grupo en filas de 2 columnas
for i, (grupo, items) in enumerate(HABILIDADES):
    if i % 2 == 0:  # Nueva fila cada 2 elementos
        cols = st.columns(2, gap="medium")
    
    col_idx = i % 2
    
    with cols[col_idx]:
        color_grupo = PALETA_GRUPOS.get(grupo, "#2E5EAA")
        
        # Contenedor del grupo
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #f8fafc 0%, white 100%);
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 5px solid {color_grupo};
            margin-bottom: 1rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        ">
            <h3 style="margin: 0 0 1rem 0; color: #0f172a; font-size: 1.1rem;">
                {grupo}
            </h3>
        """, unsafe_allow_html=True)
        
        # Obtener la función de gráfico para este grupo
        grafico_func, _ = graficos_por_grupo.get(grupo, (grafico_barh_simple, color_grupo))
        
        # Crear y mostrar el gráfico
        fig = grafico_func(grupo, items, color_grupo, height_px=280)
        st.pyplot(fig, use_container_width=True)
        
        # Cerrar el contenedor
        st.markdown("</div>", unsafe_allow_html=True)

st.divider()
