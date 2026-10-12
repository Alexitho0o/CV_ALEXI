import React from 'react';
import { Package, ShoppingCart, ArrowUpRight } from 'lucide-react';

// Destinos entregados por Alexi. Solo web: no altera las fuentes del PDF.
export const courseLinks = [
  {
    id: 'bodega',
    title: 'Gestión Eficiente de Bodegas y Control de Inventario',
    href: 'https://educacioncontinua.uc.cl/programas/gestion-eficiente-de-bodegas-y-control-de-inventario/?seccion_id=9083',
    icon: Package,
  },
  {
    id: 'compras',
    title: 'Gestión en Compras y Adquisiciones',
    href: 'https://educacioncontinua.uc.cl/programas/gestion-en-compras-y-adquisiciones/',
    icon: ShoppingCart,
  },
];

export default function Courses() {
  return <div id="cursos-uc" className="courses-uc" tabIndex={-1} aria-labelledby="courses-heading">
    <h4 id="courses-heading">Cursos que imparto en la UC</h4>
    <p className="courses-note">Consulta los programas en Educación Continua UC. Se abren en una pestaña nueva.</p>
    <div className="course-links">
      {courseLinks.map(({ id, title, href, icon: CourseIcon }) =>
        <a key={id} className="course-link" data-course={id} href={href}
          target="_blank" rel="noopener noreferrer"
          aria-label={`${title} — ver programa UC (abre una pestaña nueva)`}>
          <span className="course-icon"><CourseIcon size={22} strokeWidth={1.8} aria-hidden="true" /></span>
          <span className="course-copy"><strong>{title}</strong><span>Ver programa UC</span></span>
          <ArrowUpRight className="course-arrow" size={19} aria-hidden="true" />
        </a>
      )}
    </div>
  </div>;
}
