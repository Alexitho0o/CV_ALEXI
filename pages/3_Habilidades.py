# pages/3_Habilidades.py
# -*- coding: utf-8 -*-
import streamlit as st
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
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

# Detalles por categoría
st.markdown("## 📋 Detalle por Área")

col1, col2 = st.columns([1.2, 1])

with col1:
    for grupo, items in HABILIDADES:
        color_grupo = PALETA_GRUPOS.get(grupo, "#2E5EAA")
        
        skill_html = f"""
        <div class="skill-category" style="border-left-color: {color_grupo};">
            <h3>{grupo}</h3>
        """
        
        for skill, nivel in items:
            skill_html += f"""
            <div class="skill-item">
                <span class="skill-name">{skill}</span>
                <span class="skill-level">{nivel}%</span>
            </div>
            """
        
        skill_html += "</div>"
        st.markdown(skill_html, unsafe_allow_html=True)

with col2:
    st.markdown("### 🎓 Resumen")
    
    st.markdown("""
    **Data & Business Intelligence**
    - Power BI: Experto
    - Excel: Avanzado
    - Python: Intermedio
    
    **Gestión Académica**
    - Indicadores: Experto
    - Acreditación: Avanzado
    - Mejora Continua: Experto
    
    **Plataformas**
    - Banner: Avanzado
    - Moodle: Intermedio
    - Blackboard: Intermedio
    """)
    
    st.markdown("### 💡 Fortalezas")
    st.markdown("""
    ✅ Análisis profundo de datos
    ✅ Visualización profesional
    ✅ Gestión de proyectos
    ✅ Liderazgo académico
    ✅ Comunicación clara
    """)

st.divider()

st.markdown("### 📈 Nivel Promedio por Categoría")

avg_data = 85  # Promedio de Data & BI
avg_academic = 88.3  # Promedio de Gestión Académica
avg_platforms = 71.7  # Promedio de Plataformas

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📊 Data & BI", f"{avg_data}%", "Experto")
    
with col2:
    st.metric("🎓 Académica", f"{avg_academic:.0f}%", "Experto")
    
with col3:
    st.metric("💻 Plataformas", f"{avg_platforms:.0f}%", "Avanzado")
