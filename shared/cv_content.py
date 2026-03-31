"""Contenido compartido del CV (texto y estructuras de datos)."""

from typing import Any, Dict, List, Tuple

DATOS_PERSONALES: Dict[str, Any] = {
    "NOMBRE": "ALEXI MARCELO BURGOS FLORES",
    "UBICACION": "Villa Alemana, Valparaíso, Chile",
    "TELEFONO": "+56 9 4513 0486",
    "CORREO": "alexi.fs341@gmail.com",
    "LINKEDIN": "linkedin.com/in/alexiburgos",
    "TITULO": "Analista de Datos Institucionales | Docente Logística en Capacitación y Desarrollo UC | Diplomado en Evaluación de Aprendizajes PUC | Analista de Inventario y Costos | Coordinador Académico IP-CFT",
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
    ("Creatividad", [
        ("Autor y Compositor", 85),
        ("Producción Musical", 80),
        ("Edición Musical", 75),
    ]),
]

EDUCACION: List[Tuple[str, str, str]] = [
    ("Título Profesional: Ingeniería en Gestión de Operaciones Logísticas", "Instituto Profesional AIEP (Online)", "2023 – 2025"),
    ("Postítulo (Diplomado): Medición y Evaluación de Aprendizajes (160 hrs)", "Pontificia Universidad Católica de Chile (Online)", "Oct 2022 – May 2023"),
    ("Título Técnico de Nivel Superior: Logística", "CFT PUCV", "2013 – 2015"),
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
        "telefono": "+56 9 **** 9127",
        "email": "k***.m****@ipss.cl",
        "relacion": "Supervisora directa en análisis de datos e indicadores institucionales",
    },
    {
        "nombre": "Roberto Zúñiga Ruminot",
        "cargo": "Jefe de Carreras Comercio Exterior y Logística",
        "organizacion": "IP–CFT Santo Tomás Sede Vergara",
        "telefono": "+56 9 **** 1836",
        "email": "r******@santotomas.cl",
        "relacion": "Jefe directo durante coordinación de carrera en Santo Tomás",
    },
    {
        "nombre": "Francisco Gajardo Peñaloza",
        "cargo": "Jefe de Carreras Administración - Comercio Exterior y Mercados Digitales",
        "organizacion": "CFT ENAC",
        "telefono": "+56 9 **** 2130",
        "email": "f*******@enac.cl",
        "relacion": "Supervisor de docencia en Gestión de Bodega y Adquisiciones",
    },
    {
        "nombre": "Ximena Pinto Soto",
        "cargo": "Gerente de Administración y Finanzas",
        "organizacion": "Hotel Plaza San Francisco",
        "telefono": "+56 9 **** 5540",
        "email": "x*****@plazasanfrancisco.cl",
        "relacion": "Supervisora en gestión de costos e inventario hotelero",
    },
    {
        "nombre": "Tomás Kusianovich",
        "cargo": "Gerente General",
        "organizacion": "Importadora y Comercializadora GK",
        "telefono": "+56 9 **** 1783",
        "email": "t****.k**********@importadoragk.cl",
        "relacion": "Supervisor en operaciones logísticas y control de inventario",
    },
]
