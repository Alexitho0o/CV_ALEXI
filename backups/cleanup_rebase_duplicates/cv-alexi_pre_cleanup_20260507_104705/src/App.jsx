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
  toolGroups, valueProps, impactModel, quote,
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
  return <Icon size={size} color={color} strokeWidth={strokeWidth} />;
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
    <div className={`sec-title sec-title--${accent}`}>
      <span>{children}</span>
    </div>
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
        <div className="hero-kws">
          {profile.keywords.map((kw, i) => (
            <span key={i} className="kw">
              {kw}{i < profile.keywords.length - 1 && <span className="kw-sep"> | </span>}
            </span>
          ))}
        </div>
        <p className="hero-summary">{profile.summary}</p>
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
      </aside>
    </header>
  );
}

export default Hero;
