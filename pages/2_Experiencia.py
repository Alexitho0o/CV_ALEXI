# pages/2_Experiencia.py
# -*- coding: utf-8 -*-
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="Experiencia - Alexi Burgos CV", page_icon="💼", layout="wide")

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
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: white;
    padding: 2rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    text-align: center;
}

.timeline-header h2 {
    margin: 0;
    font-size: 1.8rem;
}

.timeline-header p {
    margin: 0.5rem 0 0 0;
    opacity: 0.9;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="timeline-header">
    <h2>📍 Mi Viaje Profesional</h2>
    <p>Navega por mis años de experiencia - haz clic en los puntos del camino</p>
</div>
""", unsafe_allow_html=True)

# Crear datos para el timeline
timeline_data = []
for item in EXPERIENCIA:
    for year in range(item['inicio'], item['fin'] + 1):
        timeline_data.append({
            'year': year,
            'cargos': [item['cargo']],
            'organismos': [item['organizacion']],
            'tipo': item['tipo'],
            'index': EXPERIENCIA.index(item)
        })

# Consolidar por año
years_dict = {}
for data in timeline_data:
    year = data['year']
    if year not in years_dict:
        years_dict[year] = {
            'cargos': [],
            'tipos': [],
            'indices': set()
        }
    if data['cargos'][0] not in years_dict[year]['cargos']:
        years_dict[year]['cargos'].extend(data['cargos'])
        years_dict[year]['tipos'].append(data['tipo'])
        years_dict[year]['indices'].add(data['index'])

sorted_years = sorted(years_dict.keys())

# Crear visualización con Plotly
fig = go.Figure()

# Colores por tipo
color_map = {
    'educacion': '#0891b2',
    'datos': '#059669',
    'logistica': '#7c3aed'
}

# Agregar puntos para cada año
y_positions = []
for i, year in enumerate(sorted_years):
    types = years_dict[year]['tipos']
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
    title='<b>Línea de Tiempo: 2012 - 2025</b>',
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
    "Navega por el tiempo",
    options=sorted_years,
    value=sorted_years[-1],
    label_visibility="collapsed"
)

# Mostrar experiencias del año seleccionado
st.markdown(f"### 🎯 Experiencias en {selected_year}")

year_experiences = [EXPERIENCIA[idx] for idx in years_dict[selected_year]['indices']]

if year_experiences:
    for item in year_experiences:
        if item['inicio'] <= selected_year <= item['fin']:
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

st.markdown("## 📊 Resumen Completo")

col1, col2, col3 = st.columns(3)

with col1:
    docencia_years = len([y for y in sorted_years 
                         if any(EXPERIENCIA[idx]['tipo'] == 'educacion' 
                               for idx in years_dict[y]['indices'])])
    st.metric("Años en Educación", f"{docencia_years}+")
    
with col2:
    logistica_years = len([y for y in sorted_years 
                          if any(EXPERIENCIA[idx]['tipo'] == 'logistica' 
                                for idx in years_dict[y]['indices'])])
    st.metric("Años en Logística", f"{logistica_years}+")
    
with col3:
    st.metric("Posiciones", f"{len(EXPERIENCIA)}")

st.divider()

st.markdown("### 🔍 Leyenda")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background: #0891b2; color: white; padding: 0.75rem; border-radius: 8px; text-align: center; font-weight: 600;">
    🎓 Educación Superior
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: #059669; color: white; padding: 0.75rem; border-radius: 8px; text-align: center; font-weight: 600;">
    📊 Análisis de Datos
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: #7c3aed; color: white; padding: 0.75rem; border-radius: 8px; text-align: center; font-weight: 600;">
    📦 Logística
    </div>
    """, unsafe_allow_html=True)

st.markdown("**Referencias disponibles a solicitud** 📞")

