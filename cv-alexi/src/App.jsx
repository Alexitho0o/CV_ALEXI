import { useState } from 'react';
import {
  GraduationCap, Users, Truck, Building2, LineChart, BarChart3,
  Database, CalendarDays, ClipboardList, FileCheck2, Package, BookOpen,
  Target, CheckCircle2, Phone, Mail, Linkedin, School,
  PieChart, Network, ArrowRight, Settings, Award,
} from 'lucide-react';
import {
  profile, quickFacts, areas, kpis,
  keyLogos, trayectoria, catColors, education,
  toolGroups, valueProps, interests, impactModel, quote,
} from './data.js';

const IconMap = {
  GraduationCap, Users, Truck, Building2, LineChart, BarChart3,
  Database, CalendarDays, ClipboardList, FileCheck2, Package, BookOpen,
  Target, CheckCircle2, Phone, Mail, Linkedin, School,
  PieChart, Network, ArrowRight, Settings, Award,
};

function DynIcon({ name, size = 14, color = 'currentColor', strokeWidth = 2 }) {
  const Icon = IconMap[name];
  if (!Icon) return null;
  return <Icon size={size} color={color} strokeWidth={strokeWidth} aria-hidden="true" focusable="false" />;
}

function SafeImage({ src, alt, className, style }) {
  const [failed, setFailed] = useState(false);
  if (failed) return (
    <div className={`img-fallback ${className || ''}`} style={style}>{alt?.[0] ?? '?'}</div>
  );
  return (
    <img src={src} alt={alt} className={className} style={style}
      onError={() => setFailed(true)} />
  );
}

function IconCircle({ name, size = 13, bg = '#08284d', d = 28 }) {
  return (
    <div className="ic" style={{ width: d, height: d, minWidth: d, background: bg }}>
      <DynIcon name={name} size={size} color="#fff" />
    </div>
  );
}

function SecTitle({ children, accent = 'orange' }) {
  return (
    <h2 className={`sec-title sec-title--${accent}`}>
      <span>{children}</span>
    </h2>
  );
}

/* ── HERO ─────────────────────────────────────────────────── */
function Hero() {
  return (
    <header className="cv-hero">
      <div className="hero-photo">
        <SafeImage src="/img/FOTO.png" alt="Alexi Marcelo Burgos Flores" className="photo" />
      </div>

      <div className="hero-body">
        <h1 className="hero-name">
          {profile.name.map((line, i) => <span key={i}>{line}</span>)}
        </h1>
        <h2 className="hero-title">{profile.title}</h2>
        {profile.keywords?.length > 0 && (
          <div className="hero-kws">
            {profile.keywords.map((kw, i) => (
              <span key={i} className="kw">
                {kw}{i < profile.keywords.length - 1 && <span className="kw-sep"> | </span>}
              </span>
            ))}
          </div>
        )}
        <p className="hero-summary">{profile.summary}</p>
        <div className="hero-contact">
          <a href={`mailto:${profile.email}`}>{profile.email}</a>
          <span aria-hidden="true"> · </span>
          <a href={`tel:${profile.phone.replace(/\s/g, '')}`}>{profile.phone}</a>
          <span aria-hidden="true"> · </span>
          <a href={`https://${profile.linkedin}`}>{profile.linkedin}</a>
        </div>
      </div>

      <aside className="hero-side">
        <div className="qf-list">
          {quickFacts.map((f, i) => (
            <div className="qf" key={i}>
              <IconCircle name={f.icon} size={11} bg="#f58220" d={22} />
              <div className="qf-text">
                <span className="qf-label">{f.label}</span>
                {f.sub && <span className="qf-sub">{f.sub}</span>}
              </div>
            </div>
          ))}
        </div>
        <div className="contact-box">
          <div className="contact-qr">
            <span className="qr-lbl">CONTACTO</span>
            <SafeImage src="/img/CONTACTO.png" alt="QR Contacto" className="qr-img" />
          </div>
        </div>
      </aside>
    </header>
  );
}

/* ── KPI STRIP ────────────────────────────────────────────── */
function KpiStrip() {
  return (
    <div className="cv-kpi">
      {kpis.map((k, i) => (
        <div className="kpi" key={i} style={{ '--kc': k.color }}>
          <div className="kpi-top">
            <span className="kpi-num">{k.number}</span>
            <div className="kpi-icon">
              <DynIcon name={k.icon} size={14} color={k.color} strokeWidth={1.8} />
            </div>
          </div>
          <div className="kpi-label">{k.title}</div>
          <div className="kpi-text">{k.text}</div>
        </div>
      ))}
    </div>
  );
}

/* ── ÁREAS CLAVE + VENN ───────────────────────────────────── */
function AreasSection() {
  return (
    <div className="cv-sec cv-sec--areas">
      <SecTitle>ÁREAS CLAVE</SecTitle>
      <div className="areas-row">
        <div className="areas-grid">
          {areas.map((a, i) => (
            <div className="area-card" key={i} style={{ '--ac': a.color }}>
              <div className="area-hd">
                <IconCircle name={a.icon} size={14} bg={a.color} d={30} />
                <h4>{a.title}</h4>
              </div>
              <ul>
                {a.bullets.map((b, j) => <li key={j}>{b}</li>)}
              </ul>
            </div>
          ))}
        </div>
        <div className="venn">
          <div className="venn-wrap">
            <div className="venn-c venn-op">
              <Settings size={13} color="#fff" /><span>OPERACIÓN</span>
            </div>
            <div className="venn-c venn-doc">
              <GraduationCap size={13} color="#fff" /><span>DOCENCIA</span>
            </div>
            <div className="venn-c venn-dat">
              <BarChart3 size={13} color="#fff" /><span>DATOS</span>
            </div>
            <div className="venn-center">
              <strong>IMPACTO<br />APLICADO</strong>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

/* ── TRAYECTORIA PROFESIONAL ──────────────────────────────── */
function TrayectoriaSection() {
  return (
    <div className="cv-sec cv-sec--tray">
      <SecTitle accent="blue">TRAYECTORIA PROFESIONAL</SecTitle>
      <div className="hito-list">
        {trayectoria.map((h, i) => {
          const cats = h.cats ?? [h.cat].filter(Boolean);
          const dotColor = catColors[cats[0]] ?? '#08284d';
          return (
            <article className="hito" key={i}>
              <div className="hito-logo">
                <SafeImage src={h.logo} alt={h.institution} className="hito-img" />
              </div>
              <div className="hito-text">
                <div className="hito-top-row">
                  <span className="hito-role">{h.role}</span>
                  <div className="hito-cats">
                    {cats.map(cat => (
                      <span key={cat} className="hito-cat"
                        style={{ background: catColors[cat] ?? '#08284d' }}>
                        {cat}
                      </span>
                    ))}
                  </div>
                  <span className="hito-period">{h.period}</span>
                </div>
                <span className="hito-inst">{h.institution}</span>
                {h.sub  && <span className="hito-sub">{h.sub}</span>}
                {h.desc && <span className="hito-desc">{h.desc}</span>}
              </div>
            </article>
          );
        })}
      </div>
    </div>
  );
}

/* ── FORMACION (columna derecha) ─────────────────────────── */
function FormacionSection() {
  return (
    <div className="cv-sec cv-sec--edu">
      <SecTitle accent="blue">FORMACIÓN</SecTitle>
      <div className="edu-grid">
        {education.map((e, i) => (
          <div className="edu-item" key={i}>
            <IconCircle name={e.icon} size={11} bg="#1f67c8" d={20} />
            <div>
              <div className="edu-title">{e.title}</div>
              <div className="edu-inst">{e.institution}</div>
              <div className="edu-detail">{e.detail}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

/* ── INSTITUCIONES (columna derecha, debajo de formación) ─── */
function InstSection() {
  return (
    <div className="cv-sec cv-sec--inst">
      <SecTitle accent="blue">INSTITUCIONES</SecTitle>
      <div className="logo-strip">
        {keyLogos.map((l, i) => (
          <div className="logo-chip" key={i} title={l.name}>
            <SafeImage src={l.src} alt={l.alt} className="logo-chip-img" />
          </div>
        ))}
      </div>
    </div>
  );
}

/* ── HERRAMIENTAS (columna derecha) ──────────────────────── */
function HerramientasSection() {
  return (
    <div className="cv-sec cv-sec--tools">
      <SecTitle>HERRAMIENTAS Y TECNOLOGÍAS</SecTitle>
      <div className="tool-groups">
        {toolGroups.map((g, i) => (
          <div className="tool-group" key={i}>
            <span className="tool-group-lbl" style={{ '--tg': g.color ?? '#1f67c8' }}>{g.label}</span>
            <div className="tool-tags">
              {g.items.map((t, j) => <span className="tool-tag" key={j}>{t}</span>)}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

/* ── PROPUESTA DE VALOR (columna derecha) ─────────────────── */
function ValorSection() {
  return (
    <div className="cv-sec cv-sec--valor">
      <SecTitle>PROPUESTA DE VALOR</SecTitle>
      <div className="val-list">
        {valueProps.map((v, i) => (
          <div className="val-item" key={i}>
            <IconCircle name={v.icon} size={11} bg="#f58220" d={22} />
            <div>
              <div className="val-title">{v.title}</div>
              <p className="val-text">{v.text}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

/* ── INTERESES (columna derecha) ─────────────────────────── */
function InterestsSection() {
  return (
    <div className="cv-sec cv-sec--interests">
      <SecTitle>INTERESES</SecTitle>
      <div className="interest-line">{interests.join(' · ')}</div>
    </div>
  );
}

/* ── MODELO DE IMPACTO (fila completa, sin quote al lado) ─── */
function ImpactRow() {
  return (
    <div className="cv-impact">
      <SecTitle>MODELO DE IMPACTO</SecTitle>
      <div className="impact-flow">
        {impactModel.map((s, i) => (
          <div key={i} className="impact-step-wrap">
            <div className="imp-step">
              <div className="imp-icon">
                <DynIcon name={s.icon} size={22} color="#fff" strokeWidth={1.8} />
                <span className="imp-num">{s.step}</span>
              </div>
              <div className="imp-title">{s.title}</div>
              <div className="imp-sub">
                {s.sub.split('\n').map((l, j, a) => (
                  <span key={j}>{l}{j < a.length - 1 && <br />}</span>
                ))}
              </div>
            </div>
            {i < impactModel.length - 1 && (
              <div className="imp-arrow">
                <ArrowRight size={12} color="#08284d" strokeWidth={2.5} />
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

/* ── FRASE DE CIERRE (debajo del modelo, arriba del footer) ── */
function QuoteBar() {
  return (
    <div className="cv-quote-bar">
      <span className="qb-open" aria-hidden="true">"</span>
      <p className="qb-text">{quote}</p>
      <cite className="qb-cite">— Alexi Burgos</cite>
    </div>
  );
}

/* ── FOOTER ───────────────────────────────────────────────── */
function CvFooter() {
  return (
    <footer className="cv-footer">
      <a href={`https://${profile.linkedin}`} className="footer-link">
        <Linkedin size={9} strokeWidth={2} />{profile.linkedin}
      </a>
      <span className="sep">·</span>
      <a href={`mailto:${profile.email}`} className="footer-link">
        <Mail size={9} strokeWidth={2} />{profile.email}
      </a>
      <span className="sep">·</span>
      <a href={`tel:${profile.phone}`} className="footer-link">
        <Phone size={9} strokeWidth={2} />{profile.phone}
      </a>
    </footer>
  );
}

/* ══════════════════════════════════════════════════════════
   APP ROOT
══════════════════════════════════════════════════════════ */

/* Vista lineal complementaria. Usa TODOS los mismos datos; no sustituye el CV visual. */
function AtsDocument() {
  return (
    <main className="cv cv-page ats-page" data-output-view="ats">
      <h1>{profile.name.join(' ')}</h1>
      <p className="ats-title">{profile.title}</p>
      <p className="ats-contact">{profile.email} | {profile.phone} | {profile.linkedin}</p>
      <section><h2>PERFIL PROFESIONAL</h2><p>{profile.summary}</p>
        {quickFacts.map((f,i) => <p key={i}>{f.label}{f.sub ? ` — ${f.sub}` : ''}</p>)}
      </section>
      <section><h2>INDICADORES DE TRAYECTORIA</h2>
        {kpis.map((k,i) => <p key={i}><strong>{k.number} {k.title}</strong> — {k.text}</p>)}
      </section>
      <section><h2>ÁREAS CLAVE</h2>
        {areas.map((a,i) => <div key={i}><h3>{a.title}</h3><p>{a.bullets.join(' · ')}</p></div>)}
        <p>OPERACIÓN · DOCENCIA · DATOS — IMPACTO APLICADO</p>
      </section>
      <section><h2>TRAYECTORIA PROFESIONAL</h2>
        {trayectoria.map((h,i) => <article key={i}>
          <h3>{h.role}</h3><p><strong>{h.institution}</strong></p>
          <p>{h.period} | {h.cats.join(' · ')}</p><p>{h.sub}</p><p>{h.desc}</p>
        </article>)}
      </section>
      <section><h2>FORMACIÓN</h2>{education.map((e,i) => <article key={i}>
        <h3>{e.title}</h3><p>{e.institution}</p><p>{e.detail}</p>
      </article>)}</section>
      <section><h2>INSTITUCIONES</h2><p>{keyLogos.map(l => l.name).join(' · ')}</p></section>
      <section><h2>HERRAMIENTAS Y TECNOLOGÍAS</h2>
        {toolGroups.map((g,i) => <div className="ats-tools" key={i}>
          <h3>{g.label}</h3><p>{g.items.join(' · ')}</p>
        </div>)}
      </section>
      <section><h2>PROPUESTA DE VALOR</h2>{valueProps.map((v,i) => <p key={i}>
        <strong>{v.title}</strong> {v.text}
      </p>)}</section>
      <section><h2>INTERESES</h2><p>{interests.join(' · ')}</p></section>
      <section><h2>MODELO DE IMPACTO</h2>{impactModel.map((m,i) => <p key={i}>
        <strong>{m.step}. {m.title}</strong> — {m.sub.replace(/\n/g,' ')}
      </p>)}</section>
      <p className="ats-quote">{quote} — Alexi Burgos</p>
    </main>
  );
}

export default function App() {
  const view = window.__CV_OUTPUT_VIEW__ || new URLSearchParams(window.location.search).get('view');
  if (view === 'ats') return <AtsDocument />;
  return (
    <div className="page-wrap">
      <div className="cv cv-page">
        <Hero />
        <KpiStrip />
        <div className="cv-body">
          <div className="col-left">
            <AreasSection />
            <TrayectoriaSection />
          </div>
          <div className="col-right">
            <FormacionSection />
            <InstSection />
            <HerramientasSection />
            <ValorSection />
            <InterestsSection />
          </div>
        </div>
        <ImpactRow />
        <QuoteBar />
        <CvFooter />
      </div>
    </div>
  );
}

