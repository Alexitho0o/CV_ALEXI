# pages/2_Experiencia.py
# -*- coding: utf-8 -*-
import plotly.graph_objects as go
import streamlit as st

from shared.ui_components import EXECUTIVE_HEADER_GRADIENT, render_page_header

st.set_page_config(page_title="Experiencia - Alexi Burgos CV", page_icon="💼", layout="wide")

# encabezado con nombre y subtítulo y gradient
header_gradient = EXECUTIVE_HEADER_GRADIENT
render_page_header(
    "ALEXI MARCELO BURGOS FLORES",
    "Experiencia Profesional",
    header_gradient,
)

EXPERIENCIA = [
    dict(
        cargo="Docente – Educación Continua UC (Freelance)",
        organizacion="Pontificia Universidad Católica de Chile (Remoto)",
        fechas="Jul 2025 – Actualidad",
        inicio=2025,
        fin=2025,
        tipo="educacion",
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
        inicio=2025,
        fin=2025,
        tipo="datos",
        viñetas=[
            "Recopilación, depuración y análisis de datos institucionales para gestión, mejora continua y acreditación.",
            "Construcción de indicadores: retención, aprobación, titulación, empleabilidad y satisfacción.",
            "Desarrollo de tableros Power BI y herramientas de consulta para mejorar acceso a información.",
            "Generación de reportes SIES y apoyo a auditorías, autoevaluaciones y levantamiento documental.",
        ],
    ),
    dict(
        cargo="Asistente Académico – Carreras Virtuales (Full time)",
        organizacion="CFT PUCV (Viña del Mar)",
        fechas="Mar 2024 – Ene 2025",
        inicio=2024,
        fin=2025,
        tipo="educacion",
        viñetas=[
            "Coordinación operativa de programas virtuales (Administración, Contabilidad, Adm. Pública, Logística).",
            "Gestión de acciones de captación y retención de estudiantes.",
            "Apoyo a selección y evaluación docente con estándares de calidad.",
            "Vinculación con sector público/privado para empleabilidad de egresados.",
        ],
    ),
    dict(
        cargo="Coordinador de Carrera (Administración/Logística) y Docente",
        organizacion="IP–CFT Santo Tomás (Santiago)",
        fechas="Ago 2019 – Mar 2024",
        inicio=2019,
        fin=2024,
        tipo="educacion",
        nota="Incluye sedes Estación Central y Santiago Centro",
        viñetas=[
            "Planificación académica: carga horaria, asignación docente, inscripciones y calificaciones.",
            "Supervisión de ejecución académica y cumplimiento de estándares.",
            "Docencia en Logística, Comercio Exterior y Supply Chain.",
            "Docente guía en prácticas y titulación de proyectos/portafolios.",
        ],
    ),
    dict(
        cargo="Docente Online (Freelance, Part-time)",
        organizacion="Escuela de Comercio de Santiago",
        fechas="Mar 2023 – May 2024",
        inicio=2023,
        fin=2024,
        tipo="educacion",
        viñetas=[
            "Dicta: Taller de Aplicación de Comercio Exterior",
            "Dicta: Tramitación y Valoración Aduanera",
        ],
    ),
    dict(
        cargo="Docente (Freelance, Part-time)",
        organizacion="CFT ENAC (Santiago Centro)",
        fechas="Mar 2022 – Mar 2024",
        inicio=2022,
        fin=2024,
        tipo="educacion",
        viñetas=[
            "Gestión de Bodega e Inventario",
            "Gestión de Adquisiciones y Administración de Post-Venta",
            "QA de asignatura online de gestión de almacenes",
        ],
    ),
    dict(
        cargo="Control de Costos y Asistente de Bodega",
        organizacion="Hotel Plaza San Francisco (Santiago Centro)",
        fechas="Ago 2018 – Abr 2019",
        inicio=2018,
        fin=2019,
        tipo="logistica",
        viñetas=[
            "Gestión de facturación e inventario en áreas operativas y administrativas del hotel.",
            "Apoyo en valorización y codificación de productos para control de costos del restaurante.",
        ],
    ),
    dict(
        cargo="Asistente Contable | Analista de Inventario | Encargado de Bodega",
        organizacion="Sociedad Importadora y Comercializadora GK (Providencia)",
        fechas="Jul 2015 – Ene 2018",
        inicio=2015,
        fin=2018,
        tipo="logistica",
        viñetas=[
            "Gestión de cuentas corrientes, facturación y pagos con reporte directo a gerencia.",
            "Control de inventarios periódicos/selectivos, con reportes de pérdidas y ajustes.",
            "Gestión de garantías con proveedores nacionales e internacionales.",
            "Liderazgo de recepción, almacenamiento y despacho con control RFID.",
        ],
    ),
    dict(
        cargo="Asistente de Bodega",
        organizacion="Empresas La Polar S.A | Amphora Beauty Shop | Computación Integral S.A (Valparaíso)",
        fechas="Mar 2013 – Jun 2015",
        inicio=2013,
        fin=2015,
        tipo="logistica",
        viñetas=[
            "Recepción, almacenamiento y despacho de productos de bodega.",
            "Control de mercadería recepcionada mediante RFID y labores de etiquetado.",
            "Preparación y acondicionamiento de pedidos nacionales e internacionales.",
        ],
    ),
    dict(
        cargo="Encargado de Bodega (Tienda Manuel Montt)",
        organizacion="Casa Ximena (Valparaíso)",
        fechas="May 2012 – Mar 2013",
        inicio=2012,
        fin=2013,
        tipo="logistica",
        viñetas=[
            "Supervisión de recepción, almacenamiento, reposición y despacho de productos.",
            "Implementación de conteos cíclicos y criterios merciológicos para control de stock.",
            "Gestión de boletas, facturas y guías, coordinando con ventas y proveedores.",
        ],
    ),
]


@st.cache_data(show_spinner=False)
def build_timeline_data(experiencia: list[dict]) -> tuple[list[int], dict]:
    """Precalcula años clave y mapeo de experiencias por año para mejorar rendimiento."""
    key_years = set()
    for item in experiencia:
        key_years.add(item["inicio"])
        key_years.add(item["fin"])

    sorted_years = sorted(list(key_years))
    years_dict: dict[int, dict] = {}

    for year in sorted_years:
        years_dict[year] = {
            "items": [],
            "cargos": [],
            "tipos": set(),
        }
        for item in experiencia:
            if item["inicio"] <= year <= item["fin"]:
                years_dict[year]["items"].append(item)
                years_dict[year]["cargos"].append(item["cargo"])
                years_dict[year]["tipos"].add(item["tipo"])

    return sorted_years, years_dict


@st.cache_data(show_spinner=False)
def build_position_summary(experiencia: list[dict]) -> dict[str, int]:
    """Agrupa posiciones por enfoque principal para resumen ejecutivo."""
    resumen = {
        "Docencia y Gestión Académica": 0,
        "Analítica y Control": 0,
        "Logística Operativa": 0,
    }

    for item in experiencia:
        cargo = item["cargo"].lower()
        if any(token in cargo for token in ("analista", "control de costos", "contable")):
            resumen["Analítica y Control"] += 1
        elif any(token in cargo for token in ("docente", "académico", "coordinador")):
            resumen["Docencia y Gestión Académica"] += 1
        else:
            resumen["Logística Operativa"] += 1

    return resumen

# CSS
st.markdown("""
<style>
.experience-item {
    background: #FFFFFF;
    padding: 1.55rem;
    border-radius: 12px;
    border: 1px solid #CBD5E1;
    border-left: 4px solid #0E7490;
    margin: 1rem 0 1.2rem;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.07);
}

.cargo {
    font-size: 1.17rem;
    font-weight: 900;
    color: #0F172A;
    margin-bottom: 0.3rem;
}
.org {
    font-size: 0.96rem;
    color: #475569;
    margin-bottom: 0.3rem;
}
.dates {
    font-size: 0.86rem;
    color: #0E7490;
    font-weight: 700;
    margin-bottom: 0.9rem;
    display: inline-block;
    background: #F1F5F9;
    padding: 0.35rem 0.7rem;
    border: 1px solid #CBD5E1;
    border-radius: 999px;
}
.note {
    font-size: 0.9rem;
    color: #475569;
    font-style: italic;
    margin-bottom: 1rem;
}
.bullets {
    margin-top: 0.55rem;
    padding-left: 1.25rem;
}
.bullets li {
    margin-bottom: 0.45rem;
    color: #475569;
    line-height: 1.58;
    font-size: 0.95rem;
}

.timeline-header {
    background: transparent;
    padding: 0;
    margin-bottom: 1.2rem;
    text-align: left;
}

.timeline-header h1 {
    margin: 0;
    font-size: 1.7rem;
    font-weight: 900;
    color: #0F172A;
    margin-bottom: 0.6rem;
}

.timeline-sub {
    color: #475569;
    margin: 0;
}

.area-summary {
    background: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-left: 4px solid var(--area-color);
    border-radius: 12px;
    padding: 1rem;
    box-shadow: 0 7px 18px rgba(15, 23, 42, 0.06);
    margin-bottom: 0.9rem;
}

.area-summary h3 {
    margin: 0;
    color: #0F172A;
    font-size: 1.05rem;
}

.area-summary .count {
    margin: 0.35rem 0 0;
    color: #0E7490;
    font-size: 1.45rem;
    font-family: "JetBrains Mono", "Source Code Pro", Consolas, monospace;
    font-weight: 700;
}

.area-item {
    background: #F8FAFC;
    border: 1px solid #CBD5E1;
    border-left: 3px solid var(--area-color);
    border-radius: 10px;
    padding: 0.75rem;
    margin: 0.5rem 0;
}

.area-item strong {
    color: #0F172A;
    font-size: 0.95rem;
}

.area-item small {
    color: #475569;
    font-size: 0.84rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="timeline-header">
    <h1>📍 Mi Viaje Profesional</h1>
    <p class="timeline-sub">10 posiciones profesionales en logística, educación superior y analítica institucional.</p>
</div>
""", unsafe_allow_html=True)

sorted_years, years_dict = build_timeline_data(EXPERIENCIA)

# Crear visualización con Plotly
fig = go.Figure()

# Colores por tipo
color_map = {
    'educacion': '#1E3A8A',
    'datos': '#0E7490',
    'logistica': '#475569'
}

# Agregar puntos para cada año CLAVE
for year in sorted_years:
    types = list(years_dict[year]['tipos'])
    primary_type = types[0] if types else 'logistica'
    color = color_map.get(primary_type, '#0E7490')
    
    fig.add_trace(go.Scatter(
        x=[year],
        y=[0],
        mode='markers+text',
        marker=dict(
            size=19,
            color=color,
            line=dict(color='white', width=3),
            opacity=0.85
        ),
        text=str(year),
        textposition='top center',
        textfont=dict(size=11, color='#0F172A', family='Inter'),
        hovertemplate=f'<b>{year}</b><br>' + 
                     '<br>'.join([f'📌 {cargo}' for cargo in years_dict[year]['cargos']]) +
                     '<extra></extra>',
        name=str(year)
    ))

# Agregar línea conectora
fig.add_trace(go.Scatter(
    x=sorted_years,
    y=[0] * len(sorted_years),
    mode='lines',
    line=dict(color='#CBD5E1', width=3, dash='solid'),
    hoverinfo='skip',
    showlegend=False,
    name=''
))

# Configurar layout
fig.update_layout(
    title='',
    title_x=0.5,
    title_font=dict(size=20, color='#0F172A'),
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        tickfont=dict(size=12, color='#475569'),
        range=[sorted_years[0] - 1, sorted_years[-1] + 1]
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
        range=[-1, 1]
    ),
    plot_bgcolor='#F1F5F9',
    paper_bgcolor='white',
    height=285,
    margin=dict(t=65, b=35, l=30, r=30),
    hovermode='closest',
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True, key="timeline")

st.divider()

# Selector de año
st.markdown("## 📅 Selecciona un Año")

selected_year = st.select_slider(
    "Navega por el tiempo (mostrando años clave)",
    options=sorted_years,
    value=sorted_years[-1],
    label_visibility="collapsed"
)

# Mostrar experiencias del año seleccionado
st.markdown(f"### 🎯 Experiencias en {selected_year}")

year_items = years_dict[selected_year]['items']

if year_items:
    for item in year_items:
        exp_html = f"""
        <div class="experience-item">
            <div class="cargo">{'🎓 ' if item['tipo'] == 'educacion' else '📦 ' if item['tipo'] == 'logistica' else '📊 '}{item['cargo']}</div>
            <div class="org">{item['organizacion']}</div>
            <div class="dates">{item['fechas']}</div>
        """
        
        if "nota" in item and item.get("nota"):
            exp_html += f'<div class="note">ℹ️ {item["nota"]}</div>'
        
        exp_html += '<ul class="bullets">'
        for viñeta in item["viñetas"]:
            exp_html += f'<li>{viñeta}</li>'
        exp_html += '</ul></div>'
        
        st.markdown(exp_html, unsafe_allow_html=True)
else:
    st.info("No hay experiencia registrada para este año")

st.divider()

st.markdown("## 📊 Detalle por Área")

# Organizar experiencias por tipo
experience_by_type = {
    'educacion': [],
    'datos': [],
    'logistica': []
}

for item in EXPERIENCIA:
    if item['tipo'] in experience_by_type:
        experience_by_type[item['tipo']].append(item)

# Mostrar por área
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="area-summary" style="--area-color:#1E3A8A;">
            <h3>🎓 Educación Superior</h3>
            <p class="count">"""
        + str(len(experience_by_type['educacion']))
        + """ posiciones</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    for item in experience_by_type['educacion']:
        st.markdown(
            f"""
            <div class="area-item" style="--area-color:#1E3A8A;">
                <strong>{item['cargo']}</strong><br>
                <small>{item['fechas']}</small>
            </div>
            """,
            unsafe_allow_html=True,
        )

with col2:
    st.markdown(
        """
        <div class="area-summary" style="--area-color:#0E7490;">
            <h3>📊 Analítica Institucional</h3>
            <p class="count">"""
        + str(len(experience_by_type['datos']))
        + """ posiciones</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    for item in experience_by_type['datos']:
        st.markdown(
            f"""
            <div class="area-item" style="--area-color:#0E7490;">
                <strong>{item['cargo']}</strong><br>
                <small>{item['fechas']}</small>
            </div>
            """,
            unsafe_allow_html=True,
        )

with col3:
    st.markdown(
        """
        <div class="area-summary" style="--area-color:#475569;">
            <h3>📦 Logística y Compras</h3>
            <p class="count">"""
        + str(len(experience_by_type['logistica']))
        + """ posiciones</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    for item in experience_by_type['logistica']:
        st.markdown(
            f"""
            <div class="area-item" style="--area-color:#475569;">
                <strong>{item['cargo']}</strong><br>
                <small>{item['fechas']}</small>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Trayectoria en Logística", "+13 años")
with col2:
    st.metric("Trayectoria en Educación", "+6 años")
with col3:
    st.metric("Posiciones Registradas", f"{len(EXPERIENCIA)}")

position_summary = build_position_summary(EXPERIENCIA)
col4, col5, col6 = st.columns(3)
with col4:
    st.metric("Docencia y Gestión", str(position_summary["Docencia y Gestión Académica"]))
with col5:
    st.metric("Analítica y Control", str(position_summary["Analítica y Control"]))
with col6:
    st.metric("Logística Operativa", str(position_summary["Logística Operativa"]))

st.divider()
