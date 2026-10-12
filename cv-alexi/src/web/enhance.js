/* Mejora progresiva. Texto y enlaces son utilizables sin JavaScript.
   Sin librerías de animación, contadores simulados ni contenido oculto al cargar. */
(() => {
  'use strict';
  const root = document.documentElement;
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.menu-toggle');
  const menu = document.querySelector('#site-navigation');
  const navLinks = [...document.querySelectorAll('[data-nav]')];
  const backTop = document.querySelector('.back-to-top');
  const progress = document.querySelector('.reading-progress > span');
  const motionToggle = document.querySelector('[data-motion-toggle]');
  const systemMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const compactNav = window.matchMedia('(max-width: 960px)');
  const animations = new Set();
  let userReduce = false;
  try { userReduce = sessionStorage.getItem('cv-reduce-motion') === 'true'; } catch { /* Almacenamiento opcional. */ }
  const reduceMotion = () => systemMotion.matches || userReduce;

  function applyMotionPreference() {
    const reduced = reduceMotion();
    root.classList.toggle('reduced-motion', reduced);
    if (reduced) animations.forEach(animation => animation.cancel());
    if (motionToggle) {
      motionToggle.hidden = false;
      motionToggle.disabled = systemMotion.matches;
      motionToggle.setAttribute('aria-pressed', String(reduced));
      motionToggle.textContent = systemMotion.matches ? 'Movimiento reducido (sistema)' : 'Reducir animaciones';
    }
  }
  motionToggle?.addEventListener('click', () => {
    userReduce = !userReduce;
    try { sessionStorage.setItem('cv-reduce-motion', String(userReduce)); } catch { /* No es obligatorio. */ }
    applyMotionPreference();
  });
  systemMotion.addEventListener('change', applyMotionPreference);
  applyMotionPreference();

  function closeMenu(restoreFocus = false) {
    toggle?.setAttribute('aria-expanded', 'false');
    toggle?.setAttribute('aria-label', 'Abrir menú');
    menu?.classList.remove('is-open');
    if (restoreFocus && compactNav.matches) toggle?.focus({ preventScroll: true });
  }
  toggle?.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    menu?.classList.toggle('is-open', open);
  });
  menu?.addEventListener('click', event => {
    const link = event.target.closest('a');
    if (link && menu.contains(link)) closeMenu(!link.hash);
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle?.getAttribute('aria-expanded') === 'true') closeMenu(true);
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.nav-inner')) closeMenu(menu?.contains(document.activeElement));
  });
  document.addEventListener('focusin', event => {
    if (!event.target.closest('.nav-inner')) closeMenu();
  });
  compactNav.addEventListener('change', () => closeMenu());
  root.classList.add('js');

  for (const img of document.images) {
    const fallback = () => {
      const target = img.closest('.safe-image')?.querySelector('.image-fallback');
      if (target) { img.hidden = true; target.hidden = false; }
    };
    img.addEventListener('error', fallback);
    if (img.complete && !img.naturalWidth) fallback();
  }

  function setActive(id) {
    navLinks.forEach(link => {
      if (link.dataset.nav === id) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  }
  function hashTarget(hash) {
    try { return hash && document.getElementById(decodeURIComponent(hash.slice(1))); }
    catch { return null; }
  }
  function focusTarget(target) {
    if (!target) return;
    if (!target.hasAttribute('tabindex')) target.setAttribute('tabindex', '-1');
    target.focus({ preventScroll: true });
  }
  let intent = null;
  let intentTimeout;
  function followHash(hash) {
    const target = hashTarget(hash);
    if (!target) return;
    focusTarget(target);
    intent = navLinks.some(a => a.dataset.nav === target.id) ? target.id : null;
    if (intent) setActive(intent);
    clearTimeout(intentTimeout);
    intentTimeout = setTimeout(() => { intent = null; scheduleUpdate(); }, 1000);
  }
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href^="#"]');
    if (!link || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    // Ancla nativa: conserva historial, teclado, rueda y comportamiento del navegador.
    followHash(link.hash);
  });
  window.addEventListener('hashchange', () => followHash(location.hash));

  const sections = navLinks.map(a => document.getElementById(a.dataset.nav)).filter(Boolean);
  let scheduled = false;
  function updateScrollUI() {
    scheduled = false;
    const headerHeight = header?.offsetHeight || 78;
    root.style.setProperty('--anchor-offset', `${headerHeight + 18}px`);
    const extent = root.scrollHeight - window.innerHeight;
    const ratio = extent > 0 ? Math.max(0, Math.min(1, window.scrollY / extent)) : 0;
    if (progress) progress.style.transform = `scaleX(${ratio})`;
    header?.classList.toggle('is-scrolled', window.scrollY > 12);
    if (backTop) {
      const hide = window.scrollY < 700;
      if (hide && document.activeElement === backTop) focusTarget(document.getElementById('inicio'));
      backTop.hidden = hide;
    }
    if (intent) return;
    const line = headerHeight + 30;
    const positions = sections.map(el => ({ id: el.id, rect: el.getBoundingClientRect() }));
    const containing = positions.filter(p => p.rect.top <= line && p.rect.bottom > line).sort((a,b) => b.rect.top-a.rect.top);
    const passed = positions.filter(p => p.id !== 'cursos-uc' && p.rect.top <= line).sort((a,b) => b.rect.top-a.rect.top);
    setActive(window.scrollY + window.innerHeight >= root.scrollHeight-4 ? 'contacto' : (containing[0] || passed[0])?.id || 'inicio');
  }
  function scheduleUpdate() {
    if (!scheduled) { scheduled = true; requestAnimationFrame(updateScrollUI); }
  }
  window.addEventListener('scroll', scheduleUpdate, { passive: true });
  window.addEventListener('resize', scheduleUpdate, { passive: true });
  window.addEventListener('pageshow', scheduleUpdate);
  document.fonts?.ready.then(scheduleUpdate);
  if ('ResizeObserver' in window) new ResizeObserver(scheduleUpdate).observe(document.body);
  scheduleUpdate();

  // Una sola aparición, 360 ms, desplazamiento máximo 10 px. Nunca se oculta el texto.
  function reveal(element) {
    if (reduceMotion() || !element.animate || element.contains(document.activeElement)) return;
    const animation = element.animate([
      { opacity: 0.78, transform: 'translateY(10px)' },
      { opacity: 1, transform: 'translateY(0)' },
    ], { duration: 360, easing: 'cubic-bezier(.2,.65,.3,1)', iterations: 1 });
    animations.add(animation);
    const release = () => animations.delete(animation);
    animation.onfinish = release;
    animation.oncancel = release;
  }
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        observer.unobserve(entry.target);
        reveal(entry.target);
      });
    }, { threshold: 0.08 });
    document.querySelectorAll('.area-card,.experience-content,.side-section,.impact-flow > li').forEach(el => observer.observe(el));
  }
  // El encabezado se lee de inmediato; no animamos cifras, círculos ni toda la página.
})();
