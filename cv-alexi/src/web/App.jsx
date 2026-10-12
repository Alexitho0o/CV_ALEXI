import React from 'react';
import Courses from './courses.jsx';
import { renderToStaticMarkup } from 'react-dom/server';
import {
  GraduationCap, Users, Truck, Building2, LineChart, BarChart3, Database,
  CalendarDays, ClipboardList, FileCheck2, Package, BookOpen, Target,
  CheckCircle2, Linkedin, School, PieChart, Network, ArrowRight, ArrowDown,
  ArrowUpRight, Settings, Award, Menu, X,
} from 'lucide-react';
import {
  profile, quickFacts, areas, kpis, keyLogos, trayectoria, catColors,
  education, toolGroups, valueProps, interests, impactModel, quote,
} from '../data.js';

// El CV/PDF y la web leen los mismos datos. Este componente no se importa en App.jsx.
const IconMap = {
  GraduationCap, Users, Truck, Building2, LineChart, BarChart3, Database,
  CalendarDays, ClipboardList, FileCheck2, Package, BookOpen, Target,
  CheckCircle2, Linkedin, School, PieChart, Network, ArrowRight, ArrowDown,
  ArrowUpRight, Settings, Award,
};
function Icon({ name, size = 22, ...props }) {
  const Component = IconMap[name];
  if (!Component) throw new Error(`Icono web sin registrar: ${name}`);
  return <Component size={size} strokeWidth={1.8} aria-hidden="true" {...props} />;
}
function SafeImage({ src, alt, className = '', eager = false }) {
  return <span className={`safe-image ${className}`}>
    <img src={src} alt={alt} loading={eager ? 'eager' : 'lazy'} decoding="async"
      fetchPriority={eager ? 'high' : undefined} />
    <span className="image-fallback" hidden>{alt}</span>
  </span>;
}
function Heading({ id, eyebrow, children }) {
  return <div className="section-heading">
    {eyebrow && <p className="eyebrow">{eyebrow}</p>}
    <h2 id={id}>{children}</h2><span className="section-rule" aria-hidden="true" />
  </div>;
}
const linkedin = `https://${profile.linkedin}`;
const nav = [
  ['inicio', 'Inicio'], ['experiencia', 'Trayectoria'], ['cursos-uc', 'Cursos UC'], ['educacion', 'Formación'],
  ['habilidades', 'Herramientas'], ['contacto', 'Contacto'],
];
function Navigation() {
  return <header className="site-header">
    <div className="nav-inner">
      <a className="brand" href="#inicio" aria-label="Alexi Burgos — inicio">
        <span className="brand-mark" aria-hidden="true">AB<span>.</span></span>
        <span>Alexi Burgos<small>CV profesional</small></span>
      </a>
      <button className="menu-toggle" type="button" aria-expanded="false"
        aria-controls="site-navigation" aria-label="Abrir menú">
        <Menu size={24} aria-hidden="true" /><X className="close-icon" size={24} aria-hidden="true" />
      </button>
      <nav className="navigation" id="site-navigation" aria-label="Navegación principal">
        {nav.map(([id, text]) => <a key={id} href={`#${id}`} data-nav={id}>{text}</a>)}
        <a className="nav-linkedin" href={linkedin} target="_blank" rel="noopener noreferrer"
          aria-label="Perfil de LinkedIn (abre una pestaña nueva)"><Icon name="Linkedin" size={19} /><span>LinkedIn</span></a>
      </nav>
    </div>
    <div className="reading-progress" aria-hidden="true"><span /></div>
  </header>;
}
function Hero() {
  return <section id="inicio" className="hero" aria-labelledby="nombre">
    <SafeImage className="hero-photo" src="/img/FOTO.png" alt="Alexi Marcelo Burgos Flores" eager />
    <div className="hero-body">
      <p className="eyebrow hero-eyebrow">OPERACIÓN · DOCENCIA · DATOS</p>
      <h1 id="nombre">{profile.name.map((line, i) => <span key={line}>{line}</span>)}</h1>
      <p className="hero-title">{profile.title}</p>
      <p id="perfil" className="hero-summary" data-source="profile.summary">{profile.summary}</p>
      <div className="hero-actions">
        <a className="button button-orange" href={linkedin} target="_blank" rel="noopener noreferrer">
          <Icon name="Linkedin" size={19} />Conectar en LinkedIn<Icon name="ArrowUpRight" size={18} />
        </a>
        <a className="button button-quiet" href="#experiencia">Ver trayectoria<Icon name="ArrowDown" size={18} /></a>
      </div>
    </div>
    <aside className="hero-facts" aria-label="Credenciales rápidas">
      {quickFacts.map((f) => <div className="quick-fact" key={f.label}>
        <span className="fact-icon"><Icon name={f.icon} size={19} /></span>
        <div><p>{f.label}</p>{f.sub && <small>{f.sub}</small>}</div>
      </div>)}
    </aside>
  </section>;
}
function KPIs() {
  return <section className="kpis" aria-label="Indicadores de trayectoria y docencia">
    {kpis.map((k) => <article className="kpi" key={k.title} style={{ '--accent': k.color }}>
      <div className="kpi-head"><strong>{k.number}</strong><span><Icon name={k.icon} size={23} /></span></div>
      <h2>{k.title}</h2><p>{k.text}</p>
    </article>)}
  </section>;
}
function Venn() {
  return <figure className="venn" aria-label="Intersección de operación, docencia y datos: impacto aplicado">
    <div className="venn-graphic" aria-hidden="true">
      <span className="venn-shape venn-op" /><span className="venn-shape venn-doc" /><span className="venn-shape venn-data" />
      <span className="venn-label label-op"><Icon name="Settings" size={20} />OPERACIÓN</span>
      <span className="venn-label label-doc"><Icon name="GraduationCap" size={20} />DOCENCIA</span>
      <span className="venn-label label-data"><Icon name="BarChart3" size={20} />DATOS</span>
      <strong className="venn-center">IMPACTO<br />APLICADO</strong>
    </div>
    <figcaption>Conectar para generar valor</figcaption>
  </figure>;
}
function Areas() {
  return <section className="areas-section" id="areas" aria-labelledby="areas-heading">
    <span id="competencias" className="anchor-alias" aria-hidden="true" />
    <Heading id="areas-heading" eyebrow="UN PERFIL QUE CONECTA DISCIPLINAS">Áreas clave</Heading>
    <div className="areas-layout">
      {areas.map(a => <article className="area-card" key={a.title} style={{ '--accent': a.color }}>
        <div className="area-title"><span className="area-icon"><Icon name={a.icon} size={25} /></span><h3>{a.title}</h3></div>
        <ul>{a.bullets.map(b => <li key={b}>{b}</li>)}</ul>
      </article>)}
      <Venn />
    </div>
  </section>;
}
function Experience() {
  return <section id="experiencia" className="experience-section" aria-labelledby="experience-heading">
    <Heading id="experience-heading" eyebrow="EXPERIENCIA APLICADA">Trayectoria profesional</Heading>
    <ol className="timeline">
      {trayectoria.map((h, i) => <li className="experience" key={`${h.period}-${h.role}`} style={{ '--accent': catColors[h.cats[0]] }}>
        <div className="experience-logo"><SafeImage src={h.logo} alt={h.institution.split(' · ')[0]} /></div>
        <article className="experience-content">
          <div className="experience-top"><span className="experience-date">{h.period}</span>
            <div className="badges">{h.cats.map(c => <span key={c} style={{ '--badge': catColors[c], '--badgeInk': c === 'COORDINACIÓN' ? '#08284d' : '#fff' }}>{c}</span>)}</div>
          </div>
          <h3>{h.role}</h3><p className="institution">{h.institution}</p>
          <p className="experience-sub">{h.sub}</p><p className="experience-desc" data-source={`trayectoria.${i}.desc`}>{h.desc}</p>
          {h.institution.startsWith('Pontificia Universidad Católica de Chile') && <Courses />}
        </article>
      </li>)}
    </ol>
  </section>;
}
function Education() {
  return <section id="educacion" className="side-section" aria-labelledby="education-heading">
    <Heading id="education-heading">Formación</Heading>
    <div className="education-list">{education.map(e => <article className="education-item" key={e.title}>
      <span className="side-icon"><Icon name={e.icon} size={22} /></span>
      <div><h3>{e.title}</h3><p>{e.institution}</p><small>{e.detail}</small></div>
    </article>)}</div>
  </section>;
}
function Institutions() {
  const operational = trayectoria.filter(h => h.cats.includes('LOGÍSTICA'));
  return <section className="side-section" aria-labelledby="institutions-heading">
    <Heading id="institutions-heading">Instituciones vinculadas</Heading>
    <h3 className="mini-heading">Docencia</h3>
    <div className="logos">{keyLogos.map(l => <div className="logo-tile" key={l.src}>
      <SafeImage src={l.src} alt={l.name} /><span>{l.name}</span>
    </div>)}</div>
    <h3 className="mini-heading operational-label">Experiencia operativa y empresarial</h3>
    <div className="operational-names">{operational.map(h => <p key={h.logo}>{h.institution.split(' · ').filter(x => !x.includes('/') && x !== 'Providencia' && x !== 'Santiago Centro').join(' · ')}</p>)}</div>
  </section>;
}
function Tools() {
  return <section id="habilidades" className="side-section tools-section" aria-labelledby="tools-heading">
    <Heading id="tools-heading">Herramientas y tecnologías</Heading>
    <div className="tool-groups">{toolGroups.map(g => <div className="tool-group" key={g.label} style={{ '--group': g.color }}>
      <h3>{g.label}</h3><ul>{g.items.map(t => <li key={t} data-tool>{t}</li>)}</ul>
    </div>)}</div>
  </section>;
}
function Value() {
  return <section className="side-section" aria-labelledby="value-heading">
    <Heading id="value-heading">Propuesta de valor</Heading>
    <div className="value-list">{valueProps.map(v => <article className="value-item" key={v.title}>
      <span className="side-icon orange"><Icon name={v.icon} size={21} /></span>
      <div><h3>{v.title}</h3><p>{v.text}</p></div>
    </article>)}</div>
  </section>;
}
function Impact() {
  return <section className="impact-section" id="impacto" aria-labelledby="impact-heading">
    <Heading id="impact-heading" eyebrow="DE LA NECESIDAD AL RESULTADO">Modelo de impacto</Heading>
    <ol className="impact-flow">{impactModel.map((s, i) => <li key={s.step}>
      <div className="impact-icon"><Icon name={s.icon} size={27} /><span>{s.step}</span></div>
      <h3>{s.title}</h3><p>{s.sub}</p>
      {i < impactModel.length - 1 && <span className="impact-arrow"><Icon name="ArrowRight" size={21} /></span>}
    </li>)}</ol>
  </section>;
}
function Contact() {
  return <section id="contacto" className="contact-section" aria-labelledby="contact-heading">
    <span id="referencias" className="anchor-alias" aria-hidden="true" />
    <div><p className="eyebrow">SIGAMOS EN CONTACTO</p><h2 id="contact-heading">Conversemos en LinkedIn.</h2>
      <p>Docencia, analítica institucional, gestión educativa y logística.</p></div>
    <a className="button button-orange" href={linkedin} target="_blank" rel="noopener noreferrer">
      <Icon name="Linkedin" size={22} />Ver perfil<Icon name="ArrowUpRight" size={21} />
    </a>
  </section>;
}
export default function App() {
  return <>
    <a className="skip-link" href="#contenido-principal">Saltar al contenido principal</a>
    <Navigation />
    <main id="contenido-principal" tabIndex={-1} className="site-main">
      <Hero /><KPIs /><Areas />
      <div className="cv-columns"><Experience /><aside className="cv-sidebar" aria-label="Formación, herramientas y propuesta profesional">
        <Education /><Institutions /><Tools /><Value />
        <section id="intereses" className="side-section interests-section" aria-labelledby="interests-heading">
          <Heading id="interests-heading">Intereses</Heading><p>{interests.join(' · ')}</p>
        </section>
      </aside></div>
      <Impact />
      <blockquote className="quote"><p>“{quote}”</p><cite>Alexi Burgos</cite></blockquote>
      <Contact />
    </main>
    <footer className="site-footer"><span>Alexi Marcelo Burgos Flores</span>
      <a href={linkedin} target="_blank" rel="noopener noreferrer">{profile.linkedin}<Icon name="ArrowUpRight" size={16} /></a>
      <a href="#inicio">Volver al inicio<Icon name="ArrowDown" size={16} className="rotate" /></a>
      <button type="button" className="motion-toggle" data-motion-toggle aria-pressed="false" hidden>Reducir animaciones</button>
    </footer>
    <a className="back-to-top" href="#inicio" aria-label="Volver al inicio" title="Volver al inicio" hidden>
      <Icon name="ArrowDown" size={21} className="rotate" />
    </a>
  </>;
}
export function renderDocument({ preview = true } = {}) {
  const content = renderToStaticMarkup(<App />);
  // Solo campos públicos. No se serializa profile completo al cliente.
  const schema = JSON.stringify({ '@context': 'https://schema.org', '@type': 'Person',
    name: profile.name.join(' '), jobTitle: profile.title, url: 'https://cv-alexi.vercel.app/', sameAs: [linkedin] }).replaceAll('<', '\\u003c');
  return '<!doctype html>\n' + renderToStaticMarkup(<html lang="es-CL"><head>
    <meta charSet="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Alexi Burgos | Docente UC · Analista de Datos Institucionales</title>
    <meta name="description" content={profile.summary} /><meta name="theme-color" content="#08284d" />
    <meta name="robots" content={preview ? 'noindex,nofollow' : 'index,follow'} />
    <link rel="canonical" href="https://cv-alexi.vercel.app/" />
    <meta property="og:type" content="profile" /><meta property="og:locale" content="es_CL" />
    <meta property="og:title" content="Alexi Burgos | CV profesional" /><meta property="og:description" content={profile.title} />
    <link rel="stylesheet" href="/assets/web.css" />
    <link rel="stylesheet" href="/assets/ux.css" />
    <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: schema }} />
    <script src="/assets/enhance.js" defer />
  </head><body dangerouslySetInnerHTML={{ __html: content }} /></html>);
}
