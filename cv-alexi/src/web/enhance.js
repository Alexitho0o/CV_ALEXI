/* Mejora progresiva: todo el CV está en el HTML antes de ejecutar JavaScript. */
document.documentElement.classList.add('js');
const toggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('#site-navigation');
function closeMenu(restoreFocus = false) {
  toggle?.setAttribute('aria-expanded', 'false');
  toggle?.setAttribute('aria-label', 'Abrir menú');
  menu?.classList.remove('is-open');
  if (restoreFocus) toggle?.focus();
}
toggle?.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  menu?.classList.toggle('is-open', open);
});
menu?.addEventListener('click', (e) => {
  const link = e.target.closest('a');
  if (!link || !menu.contains(link)) return;
  closeMenu();
});
document.addEventListener('keydown', e => { if (e.key === 'Escape' && toggle?.getAttribute('aria-expanded') === 'true') closeMenu(true); });
document.addEventListener('click', e => { if (!e.target.closest('.nav-inner')) closeMenu(); });
for (const img of document.images) {
  const fallback = () => {
    const target = img.closest('.safe-image')?.querySelector('.image-fallback');
    if (target) { img.hidden = true; target.hidden = false; }
  };
  img.addEventListener('error', fallback);
  if (img.complete && !img.naturalWidth) fallback();
}
const links = [...document.querySelectorAll('[data-nav]')];
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    const active = entries.filter(e => e.isIntersecting).sort((a,b) => b.intersectionRatio-a.intersectionRatio)[0];
    if (!active) return;
    links.forEach(link => {
      if (link.dataset.nav === active.target.id) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  }, { rootMargin: '-80px 0px -45% 0px', threshold: [0, .1, .3] });
  links.forEach(link => { const section = document.getElementById(link.dataset.nav); if(section) observer.observe(section); });
}
