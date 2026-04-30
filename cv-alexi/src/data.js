export const profile = {
  name: ['ALEXI MARCELO', 'BURGOS FLORES'],
  title: 'Docente UC · Especialista en Logística, Gestión Educativa y Analítica de Datos',
  keywords: ['LOGÍSTICA', 'SUPPLY CHAIN', 'GESTIÓN EDUCATIVA', 'ANALÍTICA DE DATOS'],
  summary:
    'Profesional con 13 años en logística y operaciones y 7 en gestión educativa. ' +
    'Especializado en docencia técnico-profesional, analítica institucional y mejora continua. ' +
    'Integra operación, formación y datos para fortalecer la empleabilidad y la toma de decisiones.',
  phone: '+56 9 4513 0486',
  email: 'alexi.fs341@gmail.com',
  linkedin: 'linkedin.com/in/alexiburgos',
};

export const quickFacts = [
  { icon: 'GraduationCap', label: 'Docente UC',             sub: 'Educación Continua' },
  { icon: 'Truck',          label: 'Logística · 13 años',   sub: 'Bodega · Compras · Supply Chain' },
  { icon: 'BarChart3',      label: 'Analítica de Datos',     sub: 'Power BI · Excel · Python' },
];

export const areas = [
  {
    icon: 'Truck',
    title: 'LOGÍSTICA Y SUPPLY CHAIN',
    color: '#08284d',
    bullets: ['Bodega e inventarios', 'Compras y abastecimiento', 'Transporte y distribución', 'Indicadores KPI'],
  },
  {
    icon: 'GraduationCap',
    title: 'DOCENCIA Y GESTIÓN EDUCATIVA',
    color: '#f58220',
    bullets: ['Coordinación académica', 'Metodologías activas', 'Evaluación de aprendizajes', 'Empleabilidad sectorial'],
  },
  {
    icon: 'LineChart',
    title: 'ANALÍTICA Y TECNOLOGÍA',
    color: '#1f67c8',
    bullets: ['Power BI y tableros KPI', 'Excel avanzado', 'Python básico-intermedio', 'Datos para decisión'],
  },
];

export const kpis = [
  { number: '1.300+', title: 'ESTUDIANTES',    text: 'Logística · Comercio Exterior',       icon: 'Users',       color: '#08284d' },
  { number: '55+',    title: 'IMPARTICIONES',  text: 'Carreras técnicas y profesionales',    icon: 'CalendarDays',color: '#f58220' },
  { number: '12',     title: 'UC ACTUALES',    text: '~18 estudiantes por impartición',      icon: 'Building2',   color: '#1f67c8' },
  { number: '13',     title: 'AÑOS',           text: 'Experiencia en logística y operaciones',icon: 'Clock',      color: '#08284d' },
];

/* Logos instituciones (educación): solo las más representativas */
export const keyLogos = [
  { src: '/img/UC-I-Chile_1-1-scaled.jpg',      alt: 'UC Chile',      name: 'UC Chile'         },
  { src: '/img/EXPERIENCIA-2.png',               alt: 'IPSS',          name: 'IP San Sebastián' },
  { src: '/img/logo CFT PUCV con catolica.png',  alt: 'CFT PUCV',      name: 'CFT PUCV'         },
  { src: '/img/ST Logo IP-CFT-03.png',           alt: 'Sto. Tomás',    name: 'Santo Tomás'      },
  { src: '/img/AIEP AZUL.png',                   alt: 'AIEP',          name: 'IP AIEP'          },
];

/* Trayectoria unificada: docente + operativa, más reciente primero */
export const trayectoria = [
  {
    period: '2025 – Act.',
    role: 'Docente Educación Continua',
    institution: 'Pontificia Universidad Católica de Chile',
    sub: '8 Bodega · 4 Compras · ~18 estudiantes/impartición',
    logo: '/img/UC-I-Chile_1-1-scaled.jpg',
    color: '#08284d',
  },
  {
    period: '2025 – Act.',
    role: 'Analista de Datos Institucional',
    institution: 'Instituto Profesional San Sebastián',
    sub: 'Acreditación · Indicadores académicos',
    logo: '/img/EXPERIENCIA-2.png',
    color: '#1f67c8',
  },
  {
    period: '2024 – 2025',
    role: 'Asistente Académico Carreras Virtuales',
    institution: 'CFT PUCV',
    sub: 'Logística · Adm. de Empresas · Comercio Exterior',
    logo: '/img/logo CFT PUCV con catolica.png',
    color: '#1f67c8',
  },
  {
    period: '2019 – 2024',
    role: 'Coordinador y Docente',
    institution: 'Sto. Tomás · ENAC · Esc. de Comercio',
    sub: 'Logística · Comercio Exterior · Supply Chain',
    logo: '/img/ST Logo IP-CFT-03.png',
    color: '#f58220',
  },
  {
    period: '2018 – 2019',
    role: 'Control de Costos · Asistente de Bodega',
    institution: 'Hotel Plaza San Francisco',
    sub: 'Inventario · Facturación · Control de costos',
    logo: '/img/HOTEL PLAZA SAN FRANCISCO.png',
    color: '#f58220',
  },
  {
    period: '2015 – 2018',
    role: 'Analista de Inventario · Encargado de Bodega',
    institution: 'Importadora GK',
    sub: 'Control RFID · Garantías · Asistente Contable',
    logo: '/img/GK - LOGO.jpg',
    color: '#08284d',
  },
  {
    period: '2012 – 2015',
    role: 'Asistente y Encargado de Bodega',
    institution: 'La Polar · Amphora · Cintegral · Casa Ximena',
    sub: 'Recepción · Despacho · Control RFID · Reposición',
    logo: '/img/LA POLAR.jpg',
    color: '#1f67c8',
  },
];

export const education = [
  {
    title: 'Ingeniería en Gestión de Operaciones Logísticas',
    institution: 'IP AIEP',
    detail: 'Titulado · 2023–2025',
    icon: 'GraduationCap',
  },
  {
    title: 'Diplomado en Medición y Evaluación de Aprendizajes',
    institution: 'Pontificia Universidad Católica de Chile',
    detail: '160 hrs pedagógicas',
    icon: 'FileCheck2',
  },
  {
    title: 'Técnico de Nivel Superior en Logística',
    institution: 'CFT PUCV',
    detail: 'Titulado · 2013–2015',
    icon: 'Package',
  },
  {
    title: 'Certificación en Docencia Educación Superior',
    institution: 'Pontificia Universidad Católica de Chile',
    detail: 'En proceso',
    icon: 'Award',
  },
];

export const toolGroups = [
  { label: 'Analítica',      items: ['Power BI', 'Excel Avanzado', 'Python'] },
  { label: 'Académico',      items: ['Banner', 'Bettersoft U+', 'Moodle', 'Blackboard'] },
  { label: 'Productividad',  items: ['Office 365', 'GSuite'] },
];

export const valueProps = [
  { icon: 'Network',   title: 'Conecta operación, docencia y analítica', text: 'para resolver brechas formativas y operacionales.' },
  { icon: 'BookOpen',  title: 'Diseña experiencias formativas aplicadas', text: 'en logística, compras, inventario y abastecimiento.' },
  { icon: 'PieChart',  title: 'Transforma datos en indicadores útiles',   text: 'para gestión, acreditación, retención y mejora.' },
  { icon: 'Target',    title: 'Fortalece la empleabilidad',               text: 'mediante formación conectada al sector productivo.' },
];

export const impactModel = [
  { step: '1', title: 'Necesidad',      sub: 'Desafíos operativos\no formativos',     icon: 'Target'        },
  { step: '2', title: 'Diagnóstico',    sub: 'Datos, indicadores\ny contexto',         icon: 'Database'      },
  { step: '3', title: 'Diseño',         sub: 'Contenidos, metodología\ny evaluación',  icon: 'ClipboardList' },
  { step: '4', title: 'Implementación', sub: 'Acompañamiento\ny ajuste continuo',      icon: 'CheckCircle2'  },
  { step: '5', title: 'Resultados',     sub: 'Aprendizaje e impacto\nmedible',         icon: 'BarChart3'     },
];

export const quote =
  'La formacion aplicada genera valor cuando conecta operacion, datos y personas.';
