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
    ("Sistemas Operativos y Dispositivos", [
        ("MacOS", 95),
        ("Windows", 90),
        ("iOS", 90),
        ("Android (intermedio)", 75),
    ]),
    ("Herramientas Ofimáticas y Colaboración", [
        ("MS Office 365 (Word, Excel, PowerPoint)", 95),
        ("GSuite (Gmail, Docs, Sheets, Meet)", 90),
        ("Kahoot (evaluación gamificada)", 85),
        ("Mentimeter (encuestas interactivas)", 85),
    ]),
    ("Creatividad", [
        ("Autor y Compositor", 85),
        ("Producción Musical", 80),
        ("Edición Musical", 75),
    ]),
    ("Idiomas", [
        ("Inglés técnico (lectora/comprensión)", 80),
        ("Español (nativo)", 100),
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

# Diccionario de URLs de logos para herramientas (URLs verificadas y confiables)
LOGOS_URLS = {
    "Power BI": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/powerbi.svg",
    "Excel": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/microsoftexcel.svg",
    "Python": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/python.svg",
    "Moodle": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/moodle.svg",
    "BetterSoft": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/udemy.svg",
    "Banner": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/files.svg",
    "Blackboard": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/bookstack.svg",
    "Syllabus": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/google.svg",
    "MS Office": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/microsoft.svg",
    "GSuite": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/google.svg",
    "Kahoot": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/kahoot.svg",
    "Mentimeter": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/airtable.svg",
    "MacOS": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/apple.svg",
    "Windows": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/windows.svg",
    "iOS": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/ios.svg",
    "Android": "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@latest/icons/android.svg",
}

def render_logo_header(nombre_herramienta: str) -> str:
    """Genera HTML para mostrar logo uniforme de una herramienta"""
    # Buscar por coincidencia parcial del nombre
    logo_url = None
    for clave, url in LOGOS_URLS.items():
        if clave.lower() in nombre_herramienta.lower():
            logo_url = url
            break
    
    if logo_url:
        # Caja uniforme para cada logo (asegura tamaño, borde y object-fit)
        return (
            f'<div class="logo-box" title="{nombre_herramienta}">' 
            f'<img src="{logo_url}" alt="{nombre_herramienta}" />'
            f'</div>'
        )
    return ""

def grafico_barh_simple(grupo: str, items: List[Tuple[str, int]], color: str, height_px: int = 300) -> Any:
    """Gráfico horizontal para Data & BI con colores por marca"""
    skills = [s for s, _ in items]
    niveles = [n for _, n in items]
    
    fig, ax = plt.subplots(figsize=(8, height_px/100), dpi=100)
    y_pos = np.arange(len(skills))
    
    # Colores asociados a cada herramienta (identidad de marca)
    # Power BI: cyan/azul, Excel: verde, Python: azul oscuro
    colores_marca = ['#0891b2', '#059669', '#3776ab']  # PowerBI, Excel, Python
    colores_lista = colores_marca[:len(skills)]
    
    ax.barh(y_pos, niveles, color=colores_lista, alpha=0.85, edgecolor='white', linewidth=2)
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
    """Gráfico tipo donut para Plataformas Educativas con porcentajes en negro"""
    skills = [s.replace(' (', '\n(') for s, _ in items]
    niveles = [n for _, n in items]
    
    fig, ax = plt.subplots(figsize=(7, height_px/100), dpi=100)
    
    # Colores distintos por plataforma (Paired colormap)
    colors_list = plt.cm.Paired(np.linspace(0.2, 0.8, len(niveles)))
    wedges, texts, autotexts = ax.pie(
        niveles, labels=skills, autopct='%1.0f%%',
        colors=colors_list, startangle=90,
        textprops={'fontsize': 9, 'weight': '600', 'color': '#334155'},
        wedgeprops=dict(edgecolor='white', linewidth=2)
    )
    
    # Hacer el donut
    centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='#e2e8f0', linewidth=2)
    ax.add_artist(centre_circle)
    
    # Porcentajes en NEGRO (no blanco)
    for autotext in autotexts:
        autotext.set_color('#0f172a')
        autotext.set_fontweight('700')
        autotext.set_fontsize(9)
    
    fig.patch.set_facecolor('white')
    plt.tight_layout()
    return fig

def grafico_barras_verticales(grupo: str, items: List[Tuple[str, int]], color: str, height_px: int = 300) -> Any:
    """Presentación horizontal limpia para Herramientas Ofimáticas sin porcentajes"""
    skills = [s.replace(' (', '\n(') for s, _ in items]
    
    fig, ax = plt.subplots(figsize=(9, height_px/100), dpi=100)
    x_pos = np.arange(len(skills))
    
    # Colores distintos para cada herramienta ofimática
    herramienta_colores = ['#059669', '#0891b2', '#f59e0b', '#7c3aed']  # Verde, Cyan, Ámbar, Púrpura
    colores_lista = herramienta_colores[:len(skills)]
    
    # Crear barras simples sin mostrar porcentajes, solo como indicadores visuales
    ax.barh(x_pos, [1]*len(skills), color=colores_lista, alpha=0.8, edgecolor='white', linewidth=2, height=0.6)
    ax.set_yticks(x_pos)
    ax.set_yticklabels(skills, fontsize=10, fontweight='600')
    ax.set_xlim(0, 1.2)
    
    # Eliminar eje X (no mostramos valores)
    ax.set_xticks([])
    
    # Estilos limpios
    ax.grid(axis='y', alpha=0, linestyle='-')
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_color('#e2e8f0')
    
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    plt.tight_layout()
    return fig

def grafico_circular(grupo: str, items: List[Tuple[str, int]], color: str, height_px: int = 300) -> Any:
    """Gráfico circular para Sistemas Operativos"""
    skills = [s for s, _ in items]
    niveles = [n for _, n in items]
    
    fig, ax = plt.subplots(figsize=(7, height_px/100), dpi=100)
    
    sys_colors = {
        'MacOS': '#111827',
        'Windows': '#06b6d4',
        'iOS': '#8b5cf6',
        'Android (intermedio)': '#10b981',
        'Android': '#10b981'
    }
    colors_gradient = [sys_colors.get(s, '#f59e0b') for s in skills]
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
    """Gráfico horizontal para Idiomas con colores distintos por idioma"""
    skills = [s for s, _ in items]
    niveles = [n for _, n in items]
    
    fig, ax = plt.subplots(figsize=(7, height_px/100), dpi=100)
    y_pos = np.arange(len(skills))
    
    # Colores distintos para cada idioma
    idioma_colores = ['#06b6d4', '#ef4444']  # Cyan para inglés, rojo para español
    colores_lista = idioma_colores[:len(skills)]
    
    ax.barh(y_pos, niveles, color=colores_lista, alpha=0.85, edgecolor='white', linewidth=2)
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
    """Presentación conceptual para Creatividad (sin gráfica numérica)"""
    skills = [s for s, _ in items]
    
    # Para Creatividad, crear una presentación visual sin porcentajes
    fig, ax = plt.subplots(figsize=(8, height_px/100), dpi=100)
    
    # Crear texto limpio con los nombres
    y_positions = np.arange(len(skills))
    
    for i, skill in enumerate(skills):
        # Rectángulo de fondo
        rect = plt.Rectangle((0, i - 0.35), 1, 0.7, 
                             facecolor=color, 
                             edgecolor=color, 
                             alpha=0.15, 
                             linewidth=0)
        ax.add_patch(rect)
        
        # Texto del skill
        ax.text(0.05, i, f"✓ {skill}", 
               va='center', 
               ha='left', 
               fontsize=11, 
               fontweight='600',
               color='#0f172a')
    
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.5, len(skills) - 0.5)
    ax.set_aspect('auto')
    
    # Eliminar ejes
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    plt.tight_layout()
    return fig


def render_logos_and_checklist(grupo: str, items: List[Tuple[str,int]], color: str, height_px: int = 300) -> Any:
    """Muestra cobertura de habilidades mediante logos y/o lista.

    Si al menos un logo está disponible, se renderiza la rejilla de tarjetas con
    icono + nombre. Si ningún logo es reconocible (caso de Creatividad o Idiomas),
    el diseño cae en una lista de texto con checks para evitar tarjetas vacías.
    """
    # first collect logos
    logos_fragments = []
    for skill, _ in items:
        logo_html = render_logo_header(skill)
        if logo_html:
            logos_fragments.append(logo_html)

    if logos_fragments:
        # show logos in a row; each skill still aparece en la lista debajo
        st.markdown(f'<div class="logo-row">{"".join(logos_fragments)}</div>', unsafe_allow_html=True)
        # then show checklist smaller
        lista_html = '<ul style="margin:0; padding-left:1.25rem; color:#334155; font-weight:500; font-size:0.95rem;">'
        for skill, _ in items:
            lista_html += f'<li>✓ {skill}</li>'
        lista_html += '</ul>'
        st.markdown(lista_html, unsafe_allow_html=True)
    else:
        # no logos found, render only checklist with more spacing
        lista_html = '<ul style="margin:0 0 1rem 0; padding-left:1.25rem; color:#334155; font-weight:500; font-size:0.95rem;">'
        for skill, _ in items:
            lista_html += f'<li>✓ {skill}</li>'
        lista_html += '</ul>'
        st.markdown(lista_html, unsafe_allow_html=True)
    return None


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

/* Logos */
.logo-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    align-items: center;
    margin-bottom: 0.75rem;
}
.logo-box {
    width: 56px;
    height: 56px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: white;
    border-radius: 8px;
    padding: 6px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    border: 1px solid #eef2f7;
}

/* tarjetas uniformes de habilidad */
.skill-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1rem 0.5rem;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.skill-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.skill-card-name {
    margin-top: 0.5rem;
    font-size: 0.95rem;
    color: #334155;
    font-weight: 600;
}
.logo-box img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    display: block;
}

</style>
""", unsafe_allow_html=True)

# header for habilidades
header_gradient = "linear-gradient(135deg, #0891b2 0%, #06b6d4 100%)"
st.markdown(f"""
<div style="background: {header_gradient}; color: white; padding: 3rem 2rem; border-radius: 16px; margin-bottom: 2rem; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
    <h1>🎯 Habilidades y Competencias</h1>
    <p>*Especialista en análisis de datos, gestión académica y educación*</p>
</div>
""", unsafe_allow_html=True)

# Detalles por categoría con gráficos variados
st.markdown("## 📋 Detalle por Área")

# Mapeo de funciones de gráficos
graficos_por_grupo = {
    "Data & Business Intelligence": (render_logos_and_checklist, "#0891b2"),
    "Plataformas Educativas": (grafico_donut, "#7c3aed"),
    "Herramientas Ofimáticas y Colaboración": (render_logos_and_checklist, "#059669"),
    "Sistemas Operativos y Dispositivos": (render_logos_and_checklist, "#f59e0b"),
    "Creatividad": (render_logos_and_checklist, "#ec4899"),
    "Idiomas": (render_logos_and_checklist, "#ef4444"),
}

# Mostrar cada grupo con enfoque adaptativo (tarjetas o lista)
for grupo, items in HABILIDADES:
    color_grupo = PALETA_GRUPOS.get(grupo, "#2E5EAA")
    # encabezado de categoría
    st.markdown(f"""
    <div style="
        padding: 0.75rem 1rem;
        border-left: 6px solid {color_grupo};
        background: #f9fafb;
        margin-top: 1.5rem;
    ">
        <h3 style="margin:0; color:#0f172a; font-size:1.2rem; font-weight:700;">{grupo}</h3>
    </div>
    """, unsafe_allow_html=True)

    # comprobar si al menos un logo está disponible
    any_logo = any(render_logo_header(skill) for skill, _ in items)
    if any_logo:
        cols = st.columns(3, gap="small")
        for idx, (skill, _) in enumerate(items):
            with cols[idx % 3]:
                logo_html = render_logo_header(skill)
                st.markdown(f"""
                <div class="skill-card">
                    {logo_html}
                    <p class="skill-card-name">{skill}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        # no logos; usar checklist textual
        lista_html = '<ul style="margin:0 0 1rem 0; padding-left:1.25rem; color:#334155; font-weight:500; font-size:0.95rem;">'
        for skill, _ in items:
            lista_html += f'<li>✓ {skill}</li>'
        lista_html += '</ul>'
        st.markdown(lista_html, unsafe_allow_html=True)
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

st.divider()
