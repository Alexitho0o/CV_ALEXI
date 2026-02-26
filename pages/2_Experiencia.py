# pages/2_Experiencia.py
# -*- coding: utf-8 -*-
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="Experiencia - Alexi Burgos CV", page_icon="💼", layout="wide")

# header color unique for experiencia
header_color = "#7c3aed"

# encabezado con nombre y subtítulo y gradient
header_gradient = "linear-gradient(135deg, #7c3aed 0%, #a78bfa 100%)"
st.markdown(f"""
<div style="background: {header_gradient}; color: white; padding: 3rem 2rem; border-radius: 16px; margin-bottom: 2rem; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
    <h1>💼 ALEXI MARCELO BURGOS FLORES</h1>
    <p>🌟 Experiencia Profesional</p>
</div>
""", unsafe_allow_html=True)

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
        cargo="Especialista en Logística y Control de Inventarios",
        organizacion="Retail / Hotelería / Importación (Santiago–Valparaíso)",
        fechas="May 2012 – Abr 2019",
        inicio=2012,
        fin=2019,
        tipo="logistica",
        viñetas=[
            "Control de costos e inventarios multiárea y gestión de facturación/documentación.",
            "Control de inventarios, garantías y operación de bodega con RFID.",
            "Recepción, almacenamiento, picking/packing y despachos.",
        ],
    ),
]

# CSS
st.markdown("""
<style>
.experience-item {
    background: linear-gradient(135deg, #f8fafc 0%, white 100%);
    padding: 2rem;
    border-radius: 12px;
    border-left: 5px solid #0891b2;
    margin: 1.5rem 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    animation: slideIn 0.5s ease-out;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.cargo {
    font-size: 1.25rem;
    font-weight: 900;
    color: #0f172a;
    margin-bottom: 0.5rem;
}
.org {
    font-size: 1rem;
    color: #64748b;
    margin-bottom: 0.3rem;
}
.dates {
    font-size: 0.9rem;
    color: #0891b2;
    font-weight: 700;
    margin-bottom: 1rem;
    display: inline-block;
    background: rgba(8,145,178,0.1);
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
}
.note {
    font-size: 0.9rem;
    color: #64748b;
    font-style: italic;
    margin-bottom: 1rem;
}
.bullets {
    margin-top: 1rem;
    padding-left: 1.5rem;
}
.bullets li {
    margin-bottom: 0.6rem;
    color: #334155;
    line-height: 1.6;
}

.timeline-header {
    background: transparent;
    color: white;
    padding: 0;
    border-radius: 0;
    margin-bottom: 2rem;
    text-align: left;
}

.timeline-header h1 {
    margin: 0;
    font-size: 1.8rem;
    font-weight: 900;
    color: #7c3aed;
    margin-bottom: 1.5rem;
}

.timeline-header p {
    margin: 0.5rem 0 0 0;
    opacity: 0.9;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="timeline-header">
    <h1>📍 Mi Viaje Profesional</h1>
</div>
""", unsafe_allow_html=True)

# Crear datos para el timeline - SOLO AÑOS CLAVE (inicio y fin de cada posición)
key_years = set()
for item in EXPERIENCIA:
    key_years.add(item['inicio'])
    key_years.add(item['fin'])

sorted_years = sorted(list(key_years))

# Crear información por año
years_dict = {}
for year in sorted_years:
    years_dict[year] = {
        'items': [],
        'cargos': [],
        'tipos': set()
    }
    
    for item in EXPERIENCIA:
        if item['inicio'] <= year <= item['fin']:
            years_dict[year]['items'].append(item)
            years_dict[year]['cargos'].append(item['cargo'])
            years_dict[year]['tipos'].add(item['tipo'])

# Crear visualización con Plotly
fig = go.Figure()

# Colores por tipo
color_map = {
    'educacion': '#0891b2',
    'datos': '#059669',
    'logistica': '#7c3aed'
}

# Agregar puntos para cada año CLAVE
for year in sorted_years:
    types = list(years_dict[year]['tipos'])
    primary_type = types[0] if types else 'logistica'
    color = color_map.get(primary_type, '#2E5EAA')
    
    fig.add_trace(go.Scatter(
        x=[year],
        y=[0],
        mode='markers+text',
        marker=dict(
            size=20,
            color=color,
            line=dict(color='white', width=3),
            opacity=0.8
        ),
        text=str(year),
        textposition='top center',
        textfont=dict(size=11, color='#0f172a', family='Arial Black'),
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
    line=dict(color='#cbd5e1', width=3, dash='solid'),
    hoverinfo='skip',
    showlegend=False,
    name=''
))

# Configurar layout
fig.update_layout(
    title='',
    title_x=0.5,
    title_font=dict(size=20, color='#0f172a'),
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        tickfont=dict(size=12, color='#64748b'),
        range=[sorted_years[0] - 1, sorted_years[-1] + 1]
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
        range=[-1, 1]
    ),
    plot_bgcolor='rgba(248, 250, 252, 0.5)',
    paper_bgcolor='white',
    height=300,
    margin=dict(t=80, b=40, l=40, r=40),
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
    st.markdown("""
    <div style="background: #0891b2; color: white; padding: 1.5rem; border-radius: 12px; text-align: center; margin-bottom: 1rem;">
        <h3 style="margin: 0; font-size: 1.3rem;">🎓 Educación Superior</h3>
        <p style="margin: 0.5rem 0; font-size: 2rem; font-weight: bold;">""" + str(len(experience_by_type['educacion'])) + """</p>
        <p style="margin: 0; font-size: 0.9rem;">Posiciones</p>
    </div>
    """, unsafe_allow_html=True)
    
    for item in experience_by_type['educacion']:
        st.markdown(f"""
        <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border-left: 3px solid #0891b2;">
            <strong>{item['cargo']}</strong><br>
            <small style="color: #64748b;">{item['fechas']}</small>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: #059669; color: white; padding: 1.5rem; border-radius: 12px; text-align: center; margin-bottom: 1rem;">
        <h3 style="margin: 0; font-size: 1.3rem;">📊 Análisis de Datos</h3>
        <p style="margin: 0.5rem 0; font-size: 2rem; font-weight: bold;">""" + str(len(experience_by_type['datos'])) + """</p>
        <p style="margin: 0; font-size: 0.9rem;">Posiciones</p>
    </div>
    """, unsafe_allow_html=True)
    
    for item in experience_by_type['datos']:
        st.markdown(f"""
        <div style="background: #f0fdf4; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border-left: 3px solid #059669;">
            <strong>{item['cargo']}</strong><br>
            <small style="color: #64748b;">{item['fechas']}</small>
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: #7c3aed; color: white; padding: 1.5rem; border-radius: 12px; text-align: center; margin-bottom: 1rem;">
        <h3 style="margin: 0; font-size: 1.3rem;">📦 Logística y Compras</h3>
        <p style="margin: 0.5rem 0; font-size: 2rem; font-weight: bold;">""" + str(len(experience_by_type['logistica'])) + """</p>
        <p style="margin: 0; font-size: 0.9rem;">Posiciones</p>
    </div>
    """, unsafe_allow_html=True)
    
    for item in experience_by_type['logistica']:
        st.markdown(f"""
        <div style="background: #f3e8ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border-left: 3px solid #7c3aed;">
            <strong>{item['cargo']}</strong><br>
            <small style="color: #64748b;">{item['fechas']}</small>
        </div>
        """, unsafe_allow_html=True)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    docencia_years = len([y for y in sorted_years 
                         if any(item['tipo'] == 'educacion' 
                               for item in years_dict[y]['items'])])
    st.metric("Años en Educación", f"{docencia_years}+")
    
with col2:
    logistica_years = len([y for y in sorted_years 
                          if any(item['tipo'] == 'logistica' 
                                for item in years_dict[y]['items'])])
    st.metric("Años en Logística", f"{logistica_years}+")
    
with col3:
    st.metric("Posiciones", f"{len(EXPERIENCIA)}")

st.divider()

