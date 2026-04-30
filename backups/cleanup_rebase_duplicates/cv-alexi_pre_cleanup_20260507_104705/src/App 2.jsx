import { useState } from 'react';
import {
  Briefcase, GraduationCap, Users, Truck, Building2, LineChart, BarChart3,
  Database, CalendarDays, ClipboardList, FileCheck2, Package, BookOpen,
  Target, CheckCircle2, Phone, Mail, Linkedin, School,
  Monitor, PieChart, Network, ArrowRight, Settings, Clock, Award,
} from 'lucide-react';
import {
  profile, quickFacts, areas, kpis,
  institutionLogos, companyLogos, timeline, operationalTimeline, education,
  tools, valueProps, impactModel, quote,
} from './data.js';

const IconMap = {
  Briefcase, GraduationCap, Users, Truck, Building2, LineChart, BarChart3,
  Database, CalendarDays, ClipboardList, FileCheck2, Package, BookOpen,
  Target, CheckCircle2, Phone, Mail, Linkedin, School,
  Monitor, PieChart, Network, ArrowRight, Settings, Clock, Award,
};

function DynIcon({ name, size = 16, color = 'currentColor', strokeWidth = 2 }) {
  const Icon = IconMap[name];
  if (!Icon) return null;
  return <Icon size={size} color={color} strokeWidth={strokeWidth} />;
}

function SafeImage({ src, alt, className, style }) {
  const [failed, setFailed] = useState(false);
  if (failed) return (
    <div className={`img-fallback ${className || ''}`} style={style}>{alt?.[0] ?? '?'}</div>
  );
  return <img src={src} alt={alt} className={className} style={style} onError={() => setFailed(true)} />;
}

/* ── Section header ─────────────────────────────────── */
function SectionTitle({ children, accent = 'orange' }) {
  return (
    <div className={`sec-title sec-title--${accent}`}>
      <span>{children}</span>
    </div>
  );
}

/* ── Icon in colored circle ─────────────────────────── */
function IconCircle({ name, size = 14, bg = '#08284d', d = 30 }) {
  return (
    <div className="ic" style={{ width: d, height: d, minWidth: d, background: bg }}>
      <DynIcon name={name} size={size} color="#fff" />
    </div>
  );
}

/* ── Quick fact row ─────────────────────────────────── */
function QuickFact({ fact }) {
  return (
    <div className="qf">
      <IconCircle name={fact.icon} size={12} bg="#f58220" d={24} />
      <div className="qf__text">
        <span className="qf__label">{fact.label}</span>
        {fact.sub && <span className="qf__sub">{fact.sub}</span>}
      </div>
    </div>
  );
}

/* ── Logo box ───────────────────────────────────────── */
function LogoBox({ src, alt, name }) {
  return (
    <div className="logo-box" title={name?.replace('\n', ' ')}>
      <SafeImage src={src} alt={alt} className="logo-img" />
      {name && (
        <div className="logo-name">
          {name.split('\n').map((l, i) => <span key={i}>{l}</span>)}
        </div>
      )}
    </div>
  );
}

/* ── Area card ──────────────────────────────────────── */
function AreaCard({ area }) {
  return (
    <div className="area-card" style={{ '--ac': area.color }}>
      <div className="area-card__hd">
        <IconCircle name={area.icon} size={18} bg={area.color} d={38} />
        <h4>{area.title}</h4>
      </div>
      <ul>
        {area.bullets.map((b, i) => <li key={i}>{b}</li>)}
      </ul>
    </div>
  );
}

/* ── Venn diagram ───────────────────────────────────── */
function VennDiagram() {
  return (
    <div className="venn">
      <div className="venn__wrap">
        <div className="venn__c venn__op">
          <Settings size={16} color="#fff" strokeWidth={2} />
          <span>OPERACIÓN</span>
        </div>
        <div className="venn__c venn__doc">
          <GraduationCap size={16} color="#fff" strokeWidth={2} />
          <span>DOCENCIA</span>
        </div>
        <div className="venn__c venn__dat">
          <BarChart3 size={16} color="#fff" strokeWidth={2} />
          <span>DATOS</span>
        </div>
        <div className="venn__center">
          <strong>IMPACTO</strong>
          <strong>APLICADO</strong>
        </div>
      </div>
    </div>
  );
}

/* ── KPI card ───────────────────────────────────────── */
function KpiCard({ kpi }) {
  return (
    <div className="kpi" style={{ '--kc': kpi.color }}>
      <div className="kpi__top">
        <div className="kpi__num">{kpi.number}</div>
        <div className="kpi__icon">
          <DynIcon name={kpi.icon} size={22} color={kpi.color} strokeWidth={1.8} />
        </div>
      </div>
      <div className="kpi__title">{kpi.title}</div>
      <p className="kpi__text">{kpi.text}</p>
    </div>
  );
}

/* ── Timeline item ──────────────────────────────────── */
function TimelineItem({ item }) {
  return (
    <div className="tl-item">
      <div className="tl-logo" style={{ borderColor: item.color }}>
        {item.logo
          ? <SafeImage src={item.logo} alt={item.institution} className="tl-logo__img" />
          : <DynIcon name="Briefcase" size={18} color={item.color} />
        }
      </div>
      <div className="tl-period" style={{ color: item.color }}>{item.period}</div>
      <div className="tl-inst">{item.institution}</div>
      <div className="tl-role">
        {item.role.split('\n').map((l, i, a) => (
          <span key={i}>{l}{i < a.length - 1 && <br />}</span>
        ))}
      </div>
    </div>
  );
}

/* ── Education item ─────────────────────────────────── */
function EduItem({ item }) {
  return (
    <div className="edu-item">
      <IconCircle name={item.icon} size={12} bg="#1f67c8" d={24} />
      <div>
        <div className="edu-title">{item.title}</div>
        <div className="edu-inst">{item.institution}</div>
        <div className="edu-detail">{item.detail}</div>
      </div>
    </div>
  );
}

/* ── Value prop item ────────────────────────────────── */
function ValueItem({ item }) {
  return (
    <div className="val-item">
      <IconCircle name={item.icon} size={12} bg="#f58220" d={24} />
      <div>
        <div className="val-title">{item.title}</div>
        <p className="val-text">{item.text}</p>
      </div>
    </div>
  );
}

/* ── Impact step ────────────────────────────────────── */
function ImpactStep({ step, isLast }) {
  return (
    <>
      <div className="imp-step">
        <div className="imp-icon">
          <DynIcon name={step.icon} size={20} color="#fff" strokeWidth={2} />
          <span className="imp-num">{step.step}</span>
        </div>
        <div className="imp-title">{step.title}</div>
        <div className="imp-sub">
          {step.sub.split('\n').map((l, i, a) => (
            <span key={i}>{l}{i < a.length - 1 && <br />}</span>
          ))}
        </div>
      </div>
      {!isLast && (
        <div className="imp-arrow">
          <ArrowRight size={13} color="#08284d" strokeWidth={2.5} />
        </div>
      )}
    </>
  );
}

/* ══════════════════════════════════════════════════════
   APP
══════════════════════════════════════════════════════ */
export default function App() {
  return (
    <div className="page-wrap">
      <div className="cv">

        {/* ─── HERO ──────────────────────────────────── */}
        <header className="hero">
          <div className="hero__photo">
            <SafeImage src="/img/FOTO.png" alt="Alexi Marcelo Burgos Flores" className="photo" />
          </div>

          <div className="hero__body">
            <h1 className="hero__name">
              {profile.name.map((line, i) => <span key={i}>{line}</span>)}
            </h1>
            <h2 className="hero__title">{profile.title}</h2>
            <div className="hero__kws">
              {profile.keywords.map((kw, i) => (
                <span key={i} className="kw">
                  {kw}
                  {i < profile.keywords.length - 1 && <span className="kw__sep"> | </span>}
                </span>
              ))}
            </div>
            <p className="hero__summary">{profile.summary}</p>
          </div>

          <aside className="hero__side">
            <div className="qf-list">
              {quickFacts.map((f, i) => <QuickFact key={i} fact={f} />)}
            </div>
            <div className="contact-box">
              <div className="contact-qr">
                <div className="contact-qr__lbl">CONTACTO</div>
                <SafeImage src="/img/CONTACTO.jpg" alt="QR Contacto" className="qr-img" />
              </div>
              <div className="contact-links">
                <a href={`tel:${profile.phone}`} className="cl">
                  <Phone size={10} color="#f58220" strokeWidth={2.2} />{profile.phone}
                </a>
                <a href={`mailto:${profile.email}`} className="cl">
                  <Mail size={10} color="#f58220" strokeWidth={2.2} />{profile.email}
                </a>
                <a href={`https://${profile.linkedin}`} className="cl" target="_blank" rel="noopener noreferrer">
                  <Linkedin size={10} color="#f58220" strokeWidth={2.2} />{profile.linkedin}
                </a>
              </div>
            </div>
          </aside>
        </header>

        {/* ─── KPIs ──────────────────────────────────── */}
        <section className="kpi-section">
          <div className="kpi-grid">
            {kpis.map((k, i) => <KpiCard key={i} kpi={k} />)}
          </div>
        </section>

        {/* ─── ÁREAS CLAVE ───────────────────────────── */}
        <section className="cv-section">
          <SectionTitle>ÁREAS CLAVE</SectionTitle>
          <div className="areas-layout">
            <div className="areas-grid">
              {areas.map((a, i) => <AreaCard key={i} area={a} />)}
            </div>
            <VennDiagram />
          </div>
        </section>

        {/* ─── INSTITUCIONES ─────────────────────────── */}
        <section className="cv-section">
          <SectionTitle accent="blue">INSTITUCIONES DONDE HE EJERCIDO DOCENCIA Y TRABAJADO</SectionTitle>
          <div className="logos-block">
            <div className="logo-group">
              <div className="logo-group__lbl logo-group__lbl--blue">
                <GraduationCap size={10} strokeWidth={2.2} />
                EDUCACIÓN Y GESTIÓN ACADÉMICA
              </div>
              <div className="logo-row">
                {institutionLogos.map((l, i) => <LogoBox key={i} {...l} />)}
              </div>
            </div>
            <div className="logo-group">
              <div className="logo-group__lbl logo-group__lbl--orange">
                <Briefcase size={10} strokeWidth={2.2} />
                EXPERIENCIA OPERATIVA Y EMPRESARIAL
              </div>
              <div className="logo-row">
                {companyLogos.map((l, i) => <LogoBox key={i} {...l} />)}
              </div>
            </div>
          </div>
        </section>

        {/* ─── TRAYECTORIA DOCENTE ───────────────────── */}
        <section className="cv-section">
          <SectionTitle>TRAYECTORIA ACADÉMICA Y DOCENTE</SectionTitle>
          <div className="tl-track">
            <div className="tl-line" />
            <div className="tl-grid">
              {timeline.map((t, i) => <TimelineItem key={i} item={t} />)}
            </div>
          </div>
        </section>

        {/* ─── TRAYECTORIA LOGÍSTICA ─────────────────── */}
        <section className="cv-section">
          <SectionTitle accent="orange">TRAYECTORIA LOGÍSTICA Y OPERATIVA</SectionTitle>
          <div className="tl-track tl-track--op">
            <div className="tl-line tl-line--op" />
            <div className="tl-grid">
              {operationalTimeline.map((t, i) => <TimelineItem key={i} item={t} />)}
            </div>
          </div>
        </section>

        {/* ─── BOTTOM 3-COL ──────────────────────────── */}
        <div className="bottom-grid">
          <section>
            <SectionTitle accent="blue">FORMACIÓN Y CERTIFICACIONES</SectionTitle>
            <div className="edu-list">
              {education.map((e, i) => <EduItem key={i} item={e} />)}
            </div>
          </section>

          <section>
            <SectionTitle accent="blue">HERRAMIENTAS Y TECNOLOGÍAS</SectionTitle>
            <div className="tools-tags">
              {tools.map((t, i) => <span key={i} className="tool-tag">{t}</span>)}
            </div>
          </section>

          <section>
            <SectionTitle accent="blue">PROPUESTA DE VALOR</SectionTitle>
            <div className="val-list">
              {valueProps.map((v, i) => <ValueItem key={i} item={v} />)}
            </div>
          </section>
        </div>

        {/* ─── MODELO DE IMPACTO + QUOTE ─────────────── */}
        <div className="impact-row">
          <section className="impact-sec">
            <SectionTitle>MODELO DE IMPACTO</SectionTitle>
            <div className="impact-flow">
              {impactModel.map((s, i) => (
                <ImpactStep key={i} step={s} isLast={i === impactModel.length - 1} />
              ))}
            </div>
          </section>
          <blockquote className="quote">
            <span className="q-open">"</span>
            <p>{quote}</p>
            <cite>— Alexi Burgos</cite>
          </blockquote>
        </div>

        {/* ─── FOOTER ────────────────────────────────── */}
        <footer className="cv-footer">
          <a href={`https://${profile.linkedin}`} className="footer-link" target="_blank" rel="noopener noreferrer">
            <Linkedin size={10} strokeWidth={2.2} />{profile.linkedin}
          </a>
          <span className="sep">·</span>
          <a href={`mailto:${profile.email}`} className="footer-link">
            <Mail size={10} strokeWidth={2.2} />{profile.email}
          </a>
          <span className="sep">·</span>
          <a href={`tel:${profile.phone}`} className="footer-link">
            <Phone size={10} strokeWidth={2.2} />{profile.phone}
          </a>
        </footer>

      </div>
    </div>
  );
}
