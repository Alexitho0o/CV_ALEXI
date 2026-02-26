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
    "TITULO": "Docente UC | Ingeniero y Técnico en Gestión de Operaciones Logísticas",
    "RESUMEN": (
        "Soy un profesional con 13 años de experiencia en logística y 7 en gestión educativa, especializado en coordinación académica "
        "y administración de procesos educativos. Me destaco por mi capacidad para optimizar operaciones académicas, mejorar la calidad "
        "educativa y fortalecer la vinculación con el sector laboral. Poseo habilidades en liderazgo, resolución de conflictos, análisis "
        "de datos y toma de decisiones estratégicas. Puedo crear paneles de KPI y OKR en Power BI, incluyendo paneles de progreso académico, "
        "seguimiento de desempeño estudiantil y análisis de deserción académica. Además, manejo Python básico-intermedio para el análisis "
        "de bases de datos y Excel avanzado para la gestión y visualización de información."
    ),
}

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
        ("Inglés técnico (lectora/comprensión auditiva)", 80),
        ("Español (nativo)", 100),
    ]),
]

EXPERIENCIA: List[Dict[str, Any]] = [
    dict(
        cargo="Docente UC – Educación Continua",
        organizacion="Pontificia Universidad Católica de Chile (Remoto)",
        fechas="Julio 2025 – Actualidad",
        nivel="Senior | Freelance",
        viñetas=[
            "Imparto los cursos 'Gestión Eficiente de Bodegas y Control de Inventario' y 'Gestión en Compras y Adquisiciones'.",
            "Diseño y facilito contenidos actualizados sobre almacenamiento, inventarios, compras estratégicas, KPI/OKR, TCO y evaluación de proveedores.",
            "Integro metodologías activas y casos reales para aplicación inmediata de conocimientos.",
            "Enfoque orientado a reducción de costos, optimización de procesos y mejora de tiempos de respuesta.",
        ],
    ),
    dict(
        cargo="Analista de Datos Institucional – Docente",
        organizacion="Instituto Profesional San Sebastián (Híbrido)",
        fechas="Mayo 2025 – Actualidad",
        nivel="Junior | Full Time",
        viñetas=[
            "Recopilación, procesamiento y análisis de datos institucionales para gestión, mejora continua y acreditación.",
            "Elaboro indicadores clave: retención, aprobación, titulación, empleabilidad y satisfacción estudiantil.",
            "Coordino procesos de acreditación institucional, auditorías y autoevaluaciones.",
            "Desarrollo automatizaciones, tableros Power BI y herramientas de consulta para mejorar eficiencia.",
            "Genero reportes a SIES y estudios académicos de desempeño estudiantil.",
        ],
    ),
    dict(
        cargo="Asistente Académico – Carreras Virtuales",
        organizacion="CFT PUCV (Viña del Mar)",
        fechas="Marzo 2024 – Enero 2025",
        nivel="Senior | Full Time",
        viñetas=[
            "Supervisé y coordiné programas académicos de Administración, Contabilidad, Adm. Pública, Logística y Prevención de Riesgos.",
            "Gestioné acciones de captación y retención, aumentando la permanencia académica.",
            "Seleccioné y evalué personal docente, garantizando estándares de calidad educativa.",
            "Fomenté vinculación con sector público/privado para fortalecer empleabilidad de egresados.",
        ],
    ),
    dict(
        cargo="Docente Online – Comercio Exterior",
        organizacion="Escuela de Comercio de Santiago (Online)",
        fechas="Marzo 2023 – Mayo 2024",
        nivel="Senior | Freelance | Part Time",
        viñetas=[
            "Docente para asignaturas: Taller de Aplicación de Comercio Exterior y Tramitación y Valoración Aduanera.",
            "Carreras: Técnico en Comercio Exterior e Ingeniería en Comercio Internacional.",
            "Desarrollo de contenidos y evaluaciones en modalidad 100% online.",
        ],
    ),
    dict(
        cargo="Docente – Técnico en Administración y Logística",
        organizacion="CFT ENAC (Santiago Centro)",
        fechas="Marzo 2022 – Marzo 2024",
        nivel="Senior | Freelance | Part Time",
        viñetas=[
            "Docente en asignaturas: Gestión de Bodega e Inventario, Gestión de Adquisiciones y Administración de Post-Venta.",
            "Carrera: Técnico en Administración de Empresas.",
            "QA (Quality Assurance) para asignatura online Gestión de Almacenes.",
        ],
    ),
    dict(
        cargo="Coordinador de Carrera – Administración y Logística & Docente",
        organizacion="IP-CFT Santo Tomás (Sedes Estación Central y Santiago Centro)",
        fechas="Ago 2019 – Marzo 2024",
        nivel="Senior | Freelance/Full Time según período",
        viñetas=[
            "Coordinación académica: planificación, carga horaria, asignación docente, inscripciones y registro de calificaciones.",
            "Supervisión de procesos académicos, asegurando estándares de calidad y satisfacción estudiantil.",
            "Docencia en Logística, Comercio Exterior y Supply Chain Management (programas técnicos y profesionales).",
            "Docente guía y miembro de comisiones de práctica y titulación (proyectos y portafolios de evidencias).",
        ],
    ),
    dict(
        cargo="Asistente Contable | Analista de Control de Inventario | Responsable de Garantías | Encargado de Bodega",
        organizacion="Sociedad Importadora y Comercializadora GK (Providencia)",
        fechas="Julio 2015 – Enero 2018",
        nivel="Semi Senior | Full Time",
        viñetas=[
            "Gestión de cuentas corrientes, facturación y pagos, manteniendo relación directa con Gerencia.",
            "Control de inventarios periódicos y selectivos, generando reportes de pérdidas y ajustes contables.",
            "Administración de procesos de garantías con proveedores nacionales e internacionales.",
            "Liderazgo en recepción, almacenamiento y despacho de productos, implementando control con RFID.",
        ],
    ),
    dict(
        cargo="Control de Costos | Asistente de Bodega",
        organizacion="Hotel Plaza San Francisco (Santiago Centro)",
        fechas="Agosto 2018 – Abril 2019",
        nivel="Semi Senior | Full Time",
        viñetas=[
            "Gestión de facturación e inventario en múltiples áreas: Ama de llaves, recepción, bar, cocina, restaurante.",
            "Valorización y codificación de productos.",
            "Control de costos del menú del Restaurante Bristol.",
        ],
    ),
    dict(
        cargo="Asistente de Bodega",
        organizacion="Empresas La Polar | Amphora Beauty Shop | Computación Integral S.A (Valparaíso)",
        fechas="Marzo 2013 – Junio 2015",
        nivel="Junior | Full Time",
        viñetas=[
            "Recepción, almacenamiento y despacho de productos.",
            "Control mediante RFID de productos recepcionados.",
            "Labores de valor agregado: censado y etiquetado de productos.",
            "Preparación y acondicionamiento de pedidos nacionales e internacionales.",
        ],
    ),
    dict(
        cargo="Encargado de Bodega – Tienda Manuel Montt",
        organizacion="Casa Ximena (Valparaíso)",
        fechas="Mayo 2012 – Marzo 2013",
        nivel="Semi Senior | Full Time",
        viñetas=[
            "Supervisión de procesos logísticos: recepción, almacenamiento, reposición y despacho de productos.",
            "Implementación de conteos cíclicos y criterios merciológicos para optimizar almacenamiento y control de stock.",
            "Gestión de documentación operativa (boletas, facturas, guías) y orden de bodegas.",
            "Coordinación con ventas y promotores para mejorar experiencia del cliente.",
        ],
    ),
]

EDUCACION: List[Tuple[str, str, str]] = [
    ("Ingeniería en Gestión de Operaciones Logísticas (Titulado)", "Instituto Profesional AIEP (Online)", "2023 – 2025"),
    ("Diplomado en Medición y Evaluación de Aprendizajes (160 horas pedagógicas)", "Escuela de Psicología - Pontificia Universidad Católica de Santiago de Chile (Online)", "Octubre 2022 – Mayo 2023"),
    ("Técnico de Nivel Superior en Logística (Titulado)", "CFT PUCV (Valparaíso)", "2013 – 2015"),
]

COMPETENCIAS: Dict[str, str] = {
    "Gestión Académica y Tecnológica": (
        "Integración de TIC, TAC y TEP en la coordinación y gestión de procesos académicos y administrativos. "
        "Uso de tecnologías avanzadas para la planificación, evaluación y seguimiento de los aprendizajes esperados, "
        "garantizando calidad y efectividad en su implementación. Colaboración proactiva en equipos interdisciplinarios "
        "a través de plataformas digitales, asegurando la integración de recursos tecnológicos para potenciar la educación "
        "y el desarrollo profesional."
    ),
    "Metodologías y Evaluación": (
        "Modelo por competencias, metodologías de enseñanza y evaluación, diseño y validación de instrumentos de levantamiento "
        "de datos para la toma de decisiones y la mejora continua. Diseño y medición de indicadores clave de desempeño (KPI) "
        "para evaluar la efectividad de programas y procesos educativos."
    ),
    "Conocimientos Específicos": (
        "Comprensión profunda de la normativa, políticas y procedimientos que rigen los procesos educativos en la Educación "
        "Superior en Chile."
    ),
}

EQUIPAMIENTO: Dict[str, str] = {
    "Hardware": "MacBook Pro 13\" M1 2020 SSD 512 GB | Monitor Samsung de 24\" A600UCL | iPhone 15 Pro Max 256 GB | AirPods Pro (3.ª generación)",
    "Conectividad": "Internet fibra óptica VTR 900 Mbps (wifi y cable de red)",
    "Movilización": "Kia Niro 2023 | Scooter Eléctrico Mantis 8 plus",
}

INTERESES: List[str] = [
    "Gestión Educacional",
    "Producción y Edición Musical",
    "Viajes",
    "Fotografía",
    "Ciencia",
    "Tecnología",
    "Ajedrez",
    "Voleibol",
]

REFERENCIAS: List[Dict[str, str]] = [
    {
        "nombre": "Karla Muñoz Gajardo",
        "cargo": "Directora de Análisis Institucional y Estudios",
        "organizacion": "Instituto Profesional San Sebastián",
        "telefono": "+56 9 7576 9127",
        "email": "karla.munoz@ipss.cl",
    },
    {
        "nombre": "Roberto Zúñiga Ruminot",
        "cargo": "Jefe de Carreras Comercio Exterior y Logística",
        "organizacion": "IP–CFT Santo Tomás Sede Vergara",
        "telefono": "+56 9 3940 1836",
        "email": "rzuniga9@santotomas.cl",
    },
    {
        "nombre": "Francisco Gajardo Peñaloza",
        "cargo": "Jefe de Carreras Administración - Comercio Exterior y Mercados Digitales",
        "organizacion": "CFT ENAC",
        "telefono": "+56 9 78312130",
        "email": "fgajardop@enac.cl",
    },
    {
        "nombre": "Ximena Pinto Soto",
        "cargo": "Gerente de Administración y Finanzas",
        "organizacion": "Hotel Plaza San Francisco",
        "telefono": "+56 9 6496 5540",
        "email": "xpinto@plazasanfrancisco.cl",
    },
    {
        "nombre": "Tomás Kusianovich",
        "cargo": "Gerente General",
        "organizacion": "Importadora y Comercializadora GK",
        "telefono": "+56 9 5405 1783",
        "email": "tomas.kusianovich@importadoragk.cl",
    },
]

IDIOMAS = "Inglés técnico"

PALETA_GRUPOS = {
    "Data & Business Intelligence": "#0891b2",
    "Plataformas Educativas": "#7c3aed",
    "Herramientas Ofimáticas y Colaboración": "#059669",
    "Sistemas Operativos y Dispositivos": "#f59e0b",
    "Idiomas": "#ef4444",
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
    st.warning("**🎯 Competencias**\nÁreas de especialización")
with col3:
    st.error("**💻 Equipamiento**\nRecursos e intereses")

col1, col2 = st.columns(2)
with col1:
    st.info("**👥 Referencias**\nContactos profesionales")
with col2:
    st.warning("**📧 Contacto**\nCómo ponerse en contacto")
