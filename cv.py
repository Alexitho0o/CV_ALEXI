# cv.py - Home Page
# -*- coding: utf-8 -*-
import streamlit as st
from typing import Any, Dict, List, Tuple

st.set_page_config(page_title="Alexi Burgos CV", page_icon="📄", layout="wide")

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

# CSS Global
def inyectar_css() -> None:
    st.markdown("""
        <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); }
        
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
            color: #0891b2;
            font-weight: 700;
            font-size: 1.15rem;
            margin-top: 1rem;
            background: rgba(8,145,178,0.1);
            padding: 0.75rem 1rem;
            border-radius: 8px;
            display: inline-block;
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
) -> plt.Figure:
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
st.markdown(f"""
<div class="hero-header">
    <h1>🎯 {DATOS_PERSONALES['NOMBRE']}</h1>
    <div class="hero-sub">📍 {DATOS_PERSONALES['UBICACION']} | 📱 {DATOS_PERSONALES['TELEFONO']}</div>
    <div class="hero-sub">📧 {DATOS_PERSONALES['CORREO']} | 💼 {DATOS_PERSONALES['LINKEDIN']}</div>
    <div class="hero-title">{DATOS_PERSONALES['TITULO']}</div>
</div>
""", unsafe_allow_html=True)

st.markdown("## 📋 Resumen Profesional")
st.write(DATOS_PERSONALES["RESUMEN"])

st.divider()
st.markdown("## 🚀 Explora mis secciones en el menú lateral →")

col1, col2, col3 = st.columns(3)
with col1:
    st.info("**👨‍💼 Perfil**\nMi información personal")
with col2:
    st.info("**💼 Experiencia**\nHistorial laboral completo")
with col3:
    st.info("**🎯 Habilidades**\nCompetencias profesionales")

col1, col2, col3 = st.columns(3)
with col1:
    st.success("**🎓 Educación**\nFormación académica")
with col2:
    st.warning("**📧 Contacto**\nComo ponerse en contacto")
with col3:
    st.error("**📥 Descargar**\nCV en PDF (próximamente)")
