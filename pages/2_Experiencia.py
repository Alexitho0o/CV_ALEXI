# pages/2_Experiencia.py
# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(page_title="Experiencia - Alexi Burgos CV", page_icon="💼", layout="wide")

EXPERIENCIA = [
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
            "Construcción de indicadores: retención, aprobación, titulación, empleabilidad y satisfacción.",
            "Desarrollo de tableros Power BI y herramientas de consulta para mejorar acceso a información.",
            "Generación de reportes SIES y apoyo a auditorías, autoevaluaciones y levantamiento documental.",
        ],
    ),
    dict(
        cargo="Asistente Académico – Carreras Virtuales (Full time)",
        organizacion="CFT PUCV (Viña del Mar)",
        fechas="Mar 2024 – Ene 2025",
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
        viñetas=[
            "Dicta: Taller de Aplicación de Comercio Exterior",
            "Dicta: Tramitación y Valoración Aduanera",
        ],
    ),
    dict(
        cargo="Docente (Freelance, Part-time)",
        organizacion="CFT ENAC (Santiago Centro)",
        fechas="Mar 2022 – Mar 2024",
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
</style>
""", unsafe_allow_html=True)

st.markdown("# 💼 Experiencia Laboral")

st.markdown("*Más de 13 años de experiencia profesional en logística y educación superior*")

timeline = st.empty()

for idx, item in enumerate(EXPERIENCIA):
    exp_html = f"""
    <div class="experience-item">
        <div class="cargo">{'🎓 ' if 'Docente' in item['cargo'] or 'Académico' in item['cargo'] else '📊 '}{item['cargo']}</div>
        <div class="org">{item['organizacion']}</div>
        <div class="dates">{item['fechas']}</div>
    """
    
    if "nota" in item and item["nota"]:
        exp_html += f'<div class="note">ℹ️ {item["nota"]}</div>'
    
    exp_html += '<ul class="bullets">'
    for viñeta in item["viñetas"]:
        exp_html += f'<li>{viñeta}</li>'
    exp_html += '</ul></div>'
    
    st.markdown(exp_html, unsafe_allow_html=True)

st.divider()

st.markdown("## 📈 Trayectoria")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Años en Logística", "13+")
    
with col2:
    st.metric("Años en Educación", "7+")
    
with col3:
    st.metric("Posiciones", f"{len(EXPERIENCIA)}")

st.divider()

st.markdown("**Referencias disponibles a solicitud** 📞")
