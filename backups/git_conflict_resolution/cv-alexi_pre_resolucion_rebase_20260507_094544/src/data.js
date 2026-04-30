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
<<<<<<< HEAD
  { icon: 'GraduationCap', label: 'Docente UC',             sub: 'Educación Continua' },
  { icon: 'Truck',          label: 'Logística · 13 años',   sub: 'Bodega · Compras · Supply Chain' },
  { icon: 'BarChart3',      label: 'Analítica de Datos',     sub: 'Power BI · Excel · Python' },
=======
  { icon: 'GraduationCap', label: 'Docente UC · Educación Continua',   sub: null },
  { icon: 'Truck',          label: 'Logística · Supply Chain',           sub: null },
  { icon: 'BarChart3',      label: 'Analítica de Datos',                 sub: 'Power BI · Excel Avanzado · Python' },
  { icon: 'Building2',      label: 'Analista de Datos Institucional',    sub: null },
>>>>>>> 9042829 (privacy: remove phone and email from public site, keep only LinkedIn)
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
<<<<<<< HEAD
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
=======
  { number: '13+',    title: 'AÑOS LOGÍSTICA',   text: 'Operaciones · Supply Chain',             icon: 'Truck',        color: '#08284d' },
  { number: '7+',     title: 'AÑOS GESTIÓN EDUCATIVA', text: 'Docencia, coordinación y mejora formativa', icon: 'GraduationCap',color: '#f58220' },
  { number: '+1',     title: 'AÑO EN UC',        text: 'Educación Continua · 2025–Act.',         icon: 'Building2',    color: '#1f67c8' },
  { number: '+1',     title: 'AÑO ANALÍTICA',    text: 'Indicadores institucionales · IPSS',     icon: 'BarChart3',    color: '#08284d' },
  { number: '1.300+', title: 'ESTUDIANTES',       text: 'Logística · Comercio Exterior',          icon: 'Users',        color: '#f58220' },
  { number: '55+',    title: 'IMPARTICIONES',     text: 'Carreras técnicas y profesionales',      icon: 'CalendarDays', color: '#1f67c8' },
  { number: '+216',   title: 'CAPACITADOS UC',    text: '18 est. promedio × 12 imparticiones',   icon: 'Award',        color: '#08284d' },
  { number: '12',     title: 'IMPARTICIONES UC',  text: '8 Bodega · 4 Compras',                   icon: 'School',       color: '#f58220' },
];

/* Logos instituciones donde ha realizado docencia — grilla 2×2 */
export const keyLogos = [
  { src: '/img/UC-I-Chile_1-1-scaled.jpg', alt: 'UC Chile',              name: 'UC · Educación Continua'    },
  { src: '/img/ST Logo IP-CFT-03.png',     alt: 'Santo Tomás',           name: 'Santo Tomás'                },
  { src: '/img/ENAC.png',                  alt: 'ENAC',                  name: 'ENAC'                       },
  { src: '/img/camara de comercio.jpg',    alt: 'Escuela de Comercio',   name: 'Escuela de Comercio / CCS'  },
];

/* Colores fijos por categoría — no cambiar según posición */
export const catColors = {
  'DOCENCIA':     '#08284d',
  'ANALÍTICA':    '#1f67c8',
  'COORDINACIÓN': '#f58220',
  'LOGÍSTICA':    '#2d6a8f',
};

/* Trayectoria completa — cats como arreglo, period con mes y año, desc por hito */
export const trayectoria = [
  {
    period: 'Jul. 2025 – Act.',
    cats: ['DOCENCIA'],
    role: 'Docente Educación Continua',
    institution: 'Pontificia Universidad Católica de Chile',
    sub: 'Bodega · Inventario · Compras · Adquisiciones',
    desc: 'Diseño e imparto cursos de bodega, inventario, compras y adquisiciones para profesionales del área logística.',
    logo: '/img/UC-I-Chile_1-1-scaled.jpg',
  },
  {
    period: 'May. 2025 – Act.',
    cats: ['ANALÍTICA', 'DOCENCIA'],
    role: 'Analista de Datos · Docente',
    institution: 'Instituto Profesional San Sebastián',
    sub: 'Retención · Titulación · Acreditación',
    desc: 'Levanto, proceso y analizo indicadores institucionales; también imparto asignaturas online en logística.',
    logo: '/img/IPSS_png-horizontal-version-color-sin-fondo.png',
  },
  {
    period: 'Mar. 2024 – Ene. 2025',
    cats: ['COORDINACIÓN'],
    role: 'Asistente Académico — Carreras Virtuales',
    institution: 'CFT PUCV',
    sub: 'Logística · Adm. Empresas · Comercio Exterior',
    desc: 'Coordiné programas virtuales: planificación, seguimiento docente, gestión estudiantil y mejora continua.',
    logo: '/img/logo CFT PUCV con catolica.png',
  },
  {
    period: 'Mar. 2023 – May. 2024',
    cats: ['DOCENCIA'],
    role: 'Docente Online',
    institution: 'Escuela de Comercio — Cámara de Comercio de Santiago',
    sub: 'Comercio Exterior · Tramitación Aduanera',
    desc: 'Impartí comercio exterior, tramitación y valoración aduanera en programas técnicos y profesionales online.',
    logo: '/img/camara de comercio.jpg',
  },
  {
    period: 'Mar. 2022 – Mar. 2024',
    cats: ['DOCENCIA'],
    role: 'Docente y QA',
    institution: 'ENAC',
    sub: 'Bodega · Inventario · Adquisiciones · Post-Venta',
    desc: 'Impartí asignaturas de bodega, inventario, adquisiciones y postventa, y apoyé revisión de calidad online.',
    logo: '/img/ENAC.png',
  },
  {
    period: 'Ago. 2019 – Mar. 2024',
    cats: ['COORDINACIÓN', 'DOCENCIA'],
    role: 'Coordinador Académico y Docente',
    institution: 'Santo Tomás',
    sub: 'Logística · Comercio Exterior · Supply Chain',
    desc: 'Coordiné carga horaria, inscripciones, calificaciones y acompañamiento estudiantil; impartí asignaturas técnicas.',
    logo: '/img/ST Logo IP-CFT-03.png',
  },
  {
    period: 'Ago. 2018 – Abr. 2019',
    cats: ['LOGÍSTICA'],
    role: 'Asistente de Bodega y Control de Costos',
    institution: 'Hotel Plaza San Francisco',
    sub: 'Inventario · Facturación · Abastecimiento',
    desc: 'Gestioné inventario, facturación, codificación de productos y abastecimiento interno para áreas del hotel.',
    logo: '/img/HOTEL PLAZA SAN FRANCISCO.png',
  },
  {
    period: 'Jul. 2015 – Ene. 2018',
    cats: ['LOGÍSTICA'],
    role: 'Analista de Inventario y Encargado de Bodega',
    institution: 'Importadora GK',
    sub: 'Control RFID · Garantías · Trazabilidad',
    desc: 'Controlé inventarios, recepción, almacenamiento y despacho de productos, incorporando control RFID.',
    logo: '/img/GK - LOGO.jpg',
  },
  {
    period: 'May. 2012 – Jun. 2015',
    cats: ['LOGÍSTICA'],
    role: 'Asistente y Encargado de Bodega',
    institution: 'La Polar · Amphora · Cintegral · Casa Ximena',
    sub: 'Recepción · Despacho · Reposición · RFID',
    desc: 'Realicé recepción, almacenamiento, despacho, reposición y documentación operativa de pedidos.',
    logo: '/img/LA POLAR.jpg',
>>>>>>> 9042829 (privacy: remove phone and email from public site, keep only LinkedIn)
  },
];

export const education = [
  {
    title: 'Ingeniería en Gestión de Operaciones Logísticas',
<<<<<<< HEAD
    institution: 'IP AIEP',
=======
    institution: 'Instituto Profesional AIEP',
>>>>>>> 9042829 (privacy: remove phone and email from public site, keep only LinkedIn)
    detail: 'Titulado · 2023–2025',
    icon: 'GraduationCap',
  },
  {
    title: 'Diplomado en Medición y Evaluación de Aprendizajes',
    institution: 'Pontificia Universidad Católica de Chile',
<<<<<<< HEAD
    detail: '160 hrs pedagógicas',
=======
    detail: '160 hrs pedagógicas · Oct. 2022 – May. 2023',
>>>>>>> 9042829 (privacy: remove phone and email from public site, keep only LinkedIn)
    icon: 'FileCheck2',
  },
  {
    title: 'Técnico de Nivel Superior en Logística',
    institution: 'CFT PUCV',
    detail: 'Titulado · 2013–2015',
    icon: 'Package',
  },
<<<<<<< HEAD
  {
    title: 'Certificación en Docencia Educación Superior',
    institution: 'Pontificia Universidad Católica de Chile',
    detail: 'En proceso',
    icon: 'Award',
  },
=======
>>>>>>> 9042829 (privacy: remove phone and email from public site, keep only LinkedIn)
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
