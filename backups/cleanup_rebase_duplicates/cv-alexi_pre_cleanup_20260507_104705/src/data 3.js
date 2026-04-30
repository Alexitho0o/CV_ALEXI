export const profile = {
  name: ['ALEXI MARCELO', 'BURGOS FLORES'],
  title: 'Docente UC · Especialista en Logística, Gestión Educativa y Analítica de Datos',
  keywords: ['LOGÍSTICA', 'SUPPLY CHAIN', 'COMERCIO EXTERIOR', 'GESTIÓN EDUCATIVA', 'ANALÍTICA DE DATOS'],
  summary:
    'Profesional con 13 años de experiencia en logística y operaciones, y 7 años en gestión ' +
    'educativa. Especializado en docencia técnico-profesional, coordinación académica, analítica ' +
    'institucional y mejora continua. Integra operación, formación y datos para fortalecer la ' +
    'empleabilidad y apoyar la toma de decisiones mediante Power BI, Excel avanzado y Python.',
  phone: '+56 9 4513 0486',
  email: 'alexi.fs341@gmail.com',
  linkedin: 'linkedin.com/in/alexiburgos',
};

export const quickFacts = [
  { icon: 'GraduationCap', label: 'Docente y Relator',         sub: 'Logística y Operaciones' },
  { icon: 'Package',       label: 'Especialista en Bodega',    sub: 'Compras y Comercio Exterior' },
  { icon: 'School',        label: 'Educación Superior',        sub: 'Técnico-Profesional' },
  { icon: 'BarChart3',     label: 'Analista de Datos',         sub: 'IPSS · Acreditación' },
  { icon: 'Monitor',       label: 'Power BI · Excel · Python', sub: 'Avanzado / Intermedio' },
];

export const areas = [
  {
    icon: 'Truck',
    title: 'LOGÍSTICA Y SUPPLY CHAIN',
    color: '#08284d',
    bullets: [
      'Bodega e inventarios',
      'Compras y abastecimiento',
      'Transporte y distribución',
      'Control operativo e indicadores',
    ],
  },
  {
    icon: 'GraduationCap',
    title: 'DOCENCIA Y GESTIÓN EDUCATIVA',
    color: '#f58220',
    bullets: [
      'Coordinación académica',
      'Metodologías activas',
      'Evaluación de aprendizajes',
      'Empleabilidad y vinculación sectorial',
    ],
  },
  {
    icon: 'LineChart',
    title: 'ANALÍTICA Y TECNOLOGÍA',
    color: '#1f67c8',
    bullets: [
      'Power BI y tableros KPI',
      'Excel avanzado',
      'Python básico-intermedio',
      'Automatización y análisis de datos',
    ],
  },
];

export const kpis = [
  {
    number: '1.300+',
    title: 'ESTUDIANTES',
    text: 'Logística · Comercio Exterior · Empleabilidad',
    icon: 'Users',
    color: '#08284d',
  },
  {
    number: '55+',
    title: 'IMPARTICIONES',
    text: 'Carreras técnicas y profesionales',
    icon: 'CalendarDays',
    color: '#f58220',
  },
  {
    number: '12',
    title: 'UC ACTUALES',
    text: '+15 estudiantes por impartición',
    icon: 'Building2',
    color: '#1f67c8',
  },
  {
    number: '13',
    title: 'AÑOS',
    text: 'Experiencia en logística y operaciones',
    icon: 'Clock',
    color: '#08284d',
  },
];

/* Logos: ordenados por recencia (más reciente primero) */
export const institutionLogos = [
  { src: '/img/UC-I-Chile_1-1-scaled.jpg',     alt: 'UC Chile',   name: 'Pontificia\nUniversidad Católica' },
  { src: '/img/EXPERIENCIA-2.png',              alt: 'IPSS',       name: 'Instituto Prof.\nSan Sebastián' },
  { src: '/img/logo CFT PUCV con catolica.png', alt: 'CFT PUCV',   name: 'CFT PUCV' },
  { src: '/img/ST Logo IP-CFT-03.png',          alt: 'Sto Tomás',  name: 'IP-CFT\nSanto Tomás' },
  { src: '/img/ENAC.png',                       alt: 'ENAC',       name: 'CFT ENAC\nCáritas' },
  { src: '/img/camara de comercio.jpg',         alt: 'ECS',        name: 'Escuela de\nComercio' },
  { src: '/img/AIEP AZUL.png',                  alt: 'AIEP',       name: 'IP AIEP\n(U. Andrés Bello)' },
];

/* Logos empresas: ordenados cronológicamente (más reciente primero) */
export const companyLogos = [
  { src: '/img/HOTEL PLAZA SAN FRANCISCO.png',  alt: 'Hotel Plaza',     name: 'Hotel Plaza\nSan Francisco' },
  { src: '/img/GK - LOGO.jpg',                  alt: 'Importadora GK',  name: 'Importadora\nGK' },
  { src: '/img/LA POLAR.jpg',                   alt: 'La Polar',        name: 'La Polar\nS.A.' },
  { src: '/img/AMPHORA.jpg',                    alt: 'Amphora',         name: 'Amphora\nBeauty Shop' },
  { src: '/img/cintegral.png',                  alt: 'Cintegral',       name: 'Computación\nIntegral' },
  { src: '/img/casa ximena.png',                alt: 'Casa Ximena',     name: 'Casa\nXimena' },
  { src: '/img/rhein.png',                      alt: 'Rhein',           name: 'Rhein\nChile S.A.' },
];

/* Timeline docente (más reciente primero) */
export const timeline = [
  {
    logo: '/img/UC-I-Chile_1-1-scaled.jpg',
    institution: 'Pontificia Universidad Católica de Chile',
    role: 'Docente Educación Continua\n8 Bodega · 4 Compras',
    period: '2025 – Actualidad',
    color: '#08284d',
  },
  {
    logo: '/img/EXPERIENCIA-2.png',
    institution: 'Instituto Profesional San Sebastián',
    role: 'Analista de Datos Institucional\nAcreditación · Indicadores académicos',
    period: '2025 – Actualidad',
    color: '#1f67c8',
  },
  {
    logo: '/img/logo CFT PUCV con catolica.png',
    institution: 'CFT PUCV',
    role: 'Asistente Académico de Carreras Virtuales\nLogística · Adm. de Empresas · Comercio Exterior',
    period: '2024 – 2025',
    color: '#1f67c8',
  },
  {
    logo: '/img/ST Logo IP-CFT-03.png',
    institution: 'Santo Tomás · ENAC · ECS',
    role: 'Coordinador y Docente\nLogística, Comercio Exterior, Supply Chain',
    period: '2019 – 2024',
    color: '#f58220',
  },
];

/* Timeline operativo/logístico (más reciente primero) */
export const operationalTimeline = [
  {
    logo: '/img/HOTEL PLAZA SAN FRANCISCO.png',
    institution: 'Hotel Plaza San Francisco',
    role: 'Control de Costos · Asistente de Bodega\nInventario, facturación y control de costos',
    period: '2018 – 2019',
    color: '#f58220',
  },
  {
    logo: '/img/GK - LOGO.jpg',
    institution: 'Importadora GK',
    role: 'Analista de Inventario · Encargado de Bodega\nControl RFID · Garantías · Asistente Contable',
    period: '2015 – 2018',
    color: '#08284d',
  },
  {
    logo: '/img/LA POLAR.jpg',
    institution: 'La Polar · Amphora · Cintegral',
    role: 'Asistente de Bodega\nRecepción, despacho, control RFID y valor agregado',
    period: '2013 – 2015',
    color: '#1f67c8',
  },
  {
    logo: '/img/casa ximena.png',
    institution: 'Casa Ximena',
    role: 'Encargado de Bodega\nInventario, reposición, logística y despacho',
    period: '2012 – 2013',
    color: '#f58220',
  },
];

export const education = [
  {
    title: 'Ingeniería en Gestión de Operaciones Logísticas',
    institution: 'Instituto Profesional AIEP',
    detail: 'Titulado · 2023-2025',
    icon: 'GraduationCap',
  },
  {
    title: 'Diplomado en Medición y Evaluación de Aprendizajes',
    institution: 'Pontificia Universidad Católica de Chile',
    detail: '160 horas pedagógicas',
    icon: 'FileCheck2',
  },
  {
    title: 'Técnico de Nivel Superior en Logística',
    institution: 'CFT PUCV',
    detail: 'Titulado · 2013-2015',
    icon: 'Package',
  },
  {
    title: 'Certificación en Docencia para la Educación Superior',
    institution: 'Pontificia Universidad Católica de Chile',
    detail: 'En proceso',
    icon: 'Award',
  },
];

export const tools = [
  'Power BI',
  'Excel Avanzado',
  'Python Básico-Intermedio',
  'Banner (Sistema Académico)',
  'Moodle',
  'Blackboard',
  'Bettersoft U+ (Gestión Académica)',
];

export const valueProps = [
  {
    icon: 'Network',
    title: 'Conecta operación, docencia y analítica',
    text: 'para resolver brechas formativas y operacionales.',
  },
  {
    icon: 'BookOpen',
    title: 'Diseña experiencias formativas aplicadas',
    text: 'en logística, compras, inventario y abastecimiento.',
  },
  {
    icon: 'PieChart',
    title: 'Transforma datos en indicadores útiles',
    text: 'para gestión, acreditación, retención y mejora.',
  },
  {
    icon: 'Users',
    title: 'Fortalece la empleabilidad',
    text: 'mediante formación práctica conectada al sector productivo.',
  },
];

export const impactModel = [
  { step: '1', title: 'Necesidad',        sub: 'Desafíos operativos\no formativos',          icon: 'Target'       },
  { step: '2', title: 'Diagnóstico',      sub: 'Datos, indicadores\ny contexto',             icon: 'Database'     },
  { step: '3', title: 'Diseño',           sub: 'Contenidos, metodología\ny evaluación',      icon: 'ClipboardList' },
  { step: '4', title: 'Implementación',   sub: 'Acompañamiento\ny ajuste continuo',          icon: 'CheckCircle2' },
  { step: '5', title: 'Resultados',       sub: 'Aprendizaje e impacto\nmedible en personas', icon: 'BarChart3'    },
];

export const quote =
  'La formación aplicada genera valor cuando conecta operación, datos y personas.';
