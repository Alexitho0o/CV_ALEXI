# cv.py
# -*- coding: utf-8 -*-
from typing import Any, Dict, List, Tuple

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Configuración de página
st.set_page_config(page_title="Alexi Burgos CV", page_icon="📄", layout="wide")


### BLOQUE 1 - Datos estáticos del CV (sin carga, sin edición, sin exportación)
DATOS_PERSONALES: Dict[str, Any] = {
    "NOMBRE": "ALEXI MARCELO BURGOS FLORES",
    "UBICACION": "Santiago, Chile",
    "TELEFONO": "+56 9 4513 0486",
    "CORREO": "alexi.fs341@gmail.com",
    "LINKEDIN": "linkedin.com/in/alexiburgos",
    "TITULO": "ANALISTA DE DATOS INSTITUCIONAL | GESTIÓN ACADÉMICA | DOCENTE EN LOGÍSTICA",
    "RESUMEN": (
        "Ingeniero en Gestión de Operaciones Logísticas con 13 años de experiencia en logística y 7 años en educación superior. "
        "Especializado en análisis institucional, gestión académica y mejora continua. Experiencia en construcción de indicadores "
        "de retención, titulación y empleabilidad, apoyo a procesos de acreditación y desarrollo de dashboards en Power BI para "
        "toma de decisiones estratégicas. Docente en Educación Continua UC en logística, compras e inventarios."
    ),
}

HABILIDADES: List[Tuple[str, List[Tuple[str, int]]]] = [
    ("Data & Business Intelligence", [
        ("Power BI (dashboards KPI/OKR)", 90),
        ("Excel avanzado (modelamiento/visualización)", 95),
        ("Python (análisis de datos)", 70),
    ]),
    ("Gestión Académica y Calidad", [
        ("Indicadores académicos (retención/progresión)", 90),
        ("Acreditación / SIES", 85),
        ("Mejora continua", 90),
    ]),
    ("Plataformas Educativas", [
        ("Banner", 75),
        ("Moodle (intermedio)", 75),
        ("Blackboard", 65),
    ]),
]

EXPERIENCIA: List[Dict[str, Any]] = [
    dict(
        cargo="Docente – Educación Continua UC (Freelance)",
        organizacion="Pontificia Universidad Católica de Chile (Remoto)",
        fechas="Jul 2025 – Actualidad",
        viñetas=[
            "Diseño e impartición de cursos en Gestión de Bodegas y Compras Estratégicas.",
            "Integración de KPI, OKR y TCO en casos aplicados.",
            "Formación orientada a reducción de costos y optimización operativa.",
        ],
    ),
    dict(
        cargo="Analista de Datos Institucional – Docente (Full time)",
        organizacion="Instituto Profesional San Sebastián (Híbrido)",
        fechas="May 2025 – Actualidad",
        viñetas=[
            "Recopilación, depuración y análisis de datos institucionales para gestión, mejora continua y acreditación.",
            "Construcción de indicadores: retención, aprobación, titulación, empleabilidad y satisfacción (métricas no reportadas).",
            "Desarrollo de tableros Power BI y herramientas de consulta para mejorar acceso y oportunidad de información.",
            "Generación de reportes SIES y apoyo a auditorías, autoevaluaciones y levantamiento documental.",
        ],
    ),
    dict(
        cargo="Asistente Académico – Carreras Virtuales (Full time)",
        organizacion="CFT PUCV (Viña del Mar)",
        fechas="Mar 2024 – Ene 2025",
        viñetas=[
            "Coordinación operativa de programas virtuales (Administración, Contabilidad, Adm. Pública, Logística, Prev. de Riesgos).",
            "Gestión de acciones de captación y retención (métricas no reportadas).",
            "Apoyo a selección y evaluación docente, resguardando estándares de calidad y continuidad académica.",
            "Vinculación con sector público/privado para fortalecer empleabilidad de egresados.",
        ],
    ),
    dict(
        cargo="Coordinador de Carrera (Administración/Logística) y Docente",
        organizacion="IP–CFT Santo Tomás (Santiago)",
        fechas="Ago 2019 – Mar 2024",
        nota="Incluye sedes Estación Central y Santiago Centro; modalidad Freelance/Full time según período.",
        viñetas=[
            "Planificación académica: carga horaria, asignación docente, inscripciones y registro de calificaciones.",
            "Supervisión de ejecución académica y cumplimiento de estándares; gestión de requerimientos de estudiantes y docentes.",
            "Docencia en Logística, Comercio Exterior y Supply Chain (programas técnicos y profesionales).",
            "Docente guía y participación en comisiones de práctica y titulación (proyectos/portafolios).",
        ],
    ),
    dict(
        cargo="Docente Online (Freelance, Part-time)",
        organizacion="Escuela de Comercio de Santiago (Online)",
        fechas="Mar 2023 – May 2024",
        viñetas=[
            "Dicta asignaturas: Taller de Aplicación de Comercio Exterior; Tramitación y Valoración Aduanera.",
        ],
    ),
    dict(
        cargo="Docente (Freelance, Part-time)",
        organizacion="CFT ENAC (Santiago Centro)",
        fechas="Mar 2022 – Mar 2024",
        viñetas=[
            "Dicta Gestión de Bodega e Inventario, Gestión de Adquisiciones y Administración de Post-Venta.",
            "QA de asignatura online de gestión de almacenes.",
        ],
    ),
    dict(
        cargo="Experiencia previa en logística y control de inventarios",
        organizacion="Retail / Hotelería / Importación (Santiago–Valparaíso)",
        fechas="May 2012 – Abr 2019",
        viñetas=[
            "Control de costos e inventarios multiárea y gestión de facturación/documentación.",
            "Control de inventarios, garantías y operación de bodega; implementación de control con RFID.",
            "Recepción, almacenamiento, picking/packing y despachos; etiquetado/censado y control RFID.",
        ],
    ),
]

EDUCACION: List[Tuple[str, str, str]] = [
    ("Ingeniería en Gestión de Operaciones Logísticas (Titulado)", "Instituto Profesional AIEP (Online)", "2023 – 2025"),
    ("Diplomado en Medición y Evaluación de Aprendizajes (160 hrs)", "Pontificia Universidad Católica de Chile (Online)", "Oct 2022 – May 2023"),
    ("Técnico de Nivel Superior en Logística (Titulado)", "CFT PUCV", "2013 – 2015"),
]

IDIOMAS = "Inglés técnico"

PALETA_GRUPOS = {
    "Data & Business Intelligence": "#0891b2",
    "Gestión Académica y Calidad": "#059669",
    "Plataformas Educativas": "#7c3aed",
}
COLOR_PRINCIPAL = "#0f172a"
COLOR_TEXTO_SUAVE = "#475569"
COLOR_FONDO_BARRA = "#f1f5f9"

# Estilos CSS
def inyectar_css() -> None:
    st.markdown(
        """
        <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto; }
        .cv-header { padding: 2rem 0; border-bottom: 2px solid #0f172a; margin-bottom: 2rem; }
        .cv-header h1 { font-size: 2.2rem; font-weight: 900; color: #0f172a; margin-bottom: 0.25rem; letter-spacing: -0.02em; }
        .cv-sub { color: #475569; font-size: 0.95rem; margin: 0.5rem 0; font-weight: 500; }
        .cv-title { color: #0891b2; font-weight: 700; font-size: 1.05rem; margin-top: 0.75rem; }
        .section-title { color: #0f172a; font-weight: 900; letter-spacing: 0.05em; margin-top: 1.5rem; margin-bottom: 1rem; font-size: 1.15rem; text-transform: uppercase; }
        .muted { color: #64748b; font-size: 0.9rem; }
        .role { font-weight: 800; margin-bottom: 0.2rem; color: #0f172a; font-size: 1rem; }
        .org { color: #64748b; margin-top: 0.1rem; margin-bottom: 0.4rem; font-size: 0.9rem; }
        .note { color: #64748b; font-style: italic; margin-top: 0.2rem; margin-bottom: 0.4rem; font-size: 0.85rem; }
        .bullets { margin-top: 0.4rem; margin-bottom: 1rem; padding-left: 1.5rem; }
        .bullets li { margin-bottom: 0.25rem; color: #334155; font-size: 0.9rem; line-height: 1.4; }
        .card { background: white; border: 1px solid #e2e8f0; padding: 2rem; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
        </style>
        """,
        unsafe_allow_html=True,
    )

inyectar_css()

# Dashboard de habilidades
def construir_dashboard_habilidades(
    habilidades: List[Tuple[str, List[Tuple[str, int]]]],
    alto_px: int = 900,
    ancho_px: int = 1100,
    dpi: int = 180,
) -> plt.Figure:
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

    ax.barh(y, [100] * n, color="#e2e8f0", edgecolor="none", height=0.68)
    ax.barh(y, valores, color=colores, edgecolor="none", height=0.68)

    ax.set_xlim(0, 100)
    ax.set_yticks(y)
    ax.set_yticklabels(etiquetas, fontsize=9, fontweight="600", color="#1e293b")
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.tick_params(axis="x", labelsize=8, colors="#64748b", length=0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#e2e8f0")
    ax.spines["bottom"].set_color("#e2e8f0")
    ax.grid(axis="x", linestyle="--", linewidth=0.4, alpha=0.3, color="#cbd5e1")

    for i, v in enumerate(valores):
        ax.text(min(v + 1.5, 99.0), y[i], f"{v}%", va="center", ha="left", fontsize=8, color="#0f172a", fontweight="600")

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    for i in range(1, n):
        if grupos_plot[i] != grupos_plot[i - 1]:
            ax.axhline(y=y[i] + 0.5, color="#cbd5e1", linewidth=1.2, linestyle="--", alpha=0.5)

    fig.tight_layout()
    return fig

# Renderizar página CV
st.markdown(
    f"""
    <div class="cv-header">
        <h1>{DATOS_PERSONALES["NOMBRE"]}</h1>
        <div class="cv-sub">{DATOS_PERSONALES["UBICACION"]} | {DATOS_PERSONALES["TELEFONO"]} | {DATOS_PERSONALES["CORREO"]} | {DATOS_PERSONALES["LINKEDIN"]}</div>
        <div class="cv-title">{DATOS_PERSONALES["TITULO"]}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

col_izq, col_der = st.columns([1.25, 0.85], gap="large")

with col_izq:
    st.markdown('<div class="section-title">RESUMEN</div>', unsafe_allow_html=True)
    st.write(DATOS_PERSONALES["RESUMEN"])

    st.markdown('<div class="section-title">EXPERIENCIA</div>', unsafe_allow_html=True)
    for item in EXPERIENCIA:
        st.markdown(f'<div class="role">{item["cargo"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="org">{item["organizacion"]} | {item["fechas"]}</div>', unsafe_allow_html=True)
        if "nota" in item and str(item["nota"]).strip():
            st.markdown(f'<div class="note">{item["nota"]}</div>', unsafe_allow_html=True)
        st.markdown("<ul class='bullets'>" + "".join([f"<li>{b}</li>" for b in item["viñetas"]]) + "</ul>", unsafe_allow_html=True)

    st.markdown('<div class="muted">Referencias disponibles a solicitud.</div>', unsafe_allow_html=True)

with col_der:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title" style="margin-top:0.0rem;">HABILIDADES</div>', unsafe_allow_html=True)

    fig = construir_dashboard_habilidades(HABILIDADES, alto_px=920, ancho_px=980, dpi=190)
    st.pyplot(fig, clear_figure=True, use_container_width=True)

    st.markdown('<div class="section-title">EDUCACIÓN</div>', unsafe_allow_html=True)
    for grado, inst, fechas in EDUCACION:
        st.markdown(f"**{grado}**", unsafe_allow_html=True)
        st.markdown(f"<div class='muted'>{inst} | {fechas}</div>", unsafe_allow_html=True)

    st.markdown('<div class="section-title">IDIOMAS</div>', unsafe_allow_html=True)
    st.write(IDIOMAS)

    st.markdown("</div>", unsafe_allow_html=True)