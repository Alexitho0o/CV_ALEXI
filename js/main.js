document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector(".navbar");
  const navLinks = Array.from(document.querySelectorAll(".nav-link"));
  const sections = Array.from(document.querySelectorAll("main section[id]"));
  const navToggle = document.querySelector(".navbar-toggle");
  const navMenu = document.querySelector(".nav-menu");

  const getNavOffset = () => (nav ? nav.offsetHeight + 14 : 90);

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", () => {
      const isOpen = navMenu.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", String(isOpen));
    });
  }

  navLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      const hash = link.getAttribute("href");
      if (!hash || !hash.startsWith("#")) return;

      const target = document.querySelector(hash);
      if (!target) return;

      event.preventDefault();
      const top = target.getBoundingClientRect().top + window.scrollY - getNavOffset();
      window.scrollTo({ top: Math.max(top, 0), behavior: "smooth" });

      if (navMenu && navMenu.classList.contains("open")) {
        navMenu.classList.remove("open");
        if (navToggle) navToggle.setAttribute("aria-expanded", "false");
      }
    });
  });

  const setActiveLink = () => {
    const offset = getNavOffset() + 12;
    let current = sections[0]?.id || "inicio";

    sections.forEach((section) => {
      if (window.scrollY >= section.offsetTop - offset) {
        current = section.id;
      }
    });

    navLinks.forEach((link) => {
      link.classList.toggle("active", link.getAttribute("href") === `#${current}`);
    });
  };

  window.addEventListener("scroll", setActiveLink, { passive: true });
  setActiveLink();

  const revealTargets = document.querySelectorAll(".section, .experience-card, .media-slot");
  revealTargets.forEach((el) => el.classList.add("reveal"));

  const revealObserver = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("in-view");
        obs.unobserve(entry.target);
      });
    },
    { threshold: 0.15, rootMargin: "0px 0px -8% 0px" }
  );

  revealTargets.forEach((el) => revealObserver.observe(el));

  const loadImageIfExists = (slot) => {
    const existingImage = slot.querySelector("img");
    if (existingImage) {
      slot.classList.add("has-image");
      slot.classList.remove("is-empty");
      return;
    }

    const fileName = slot.getAttribute("data-image-file");
    if (!fileName) {
      slot.classList.add("is-empty");
      return;
    }

    const baseName = fileName.replace(/\.[^.]+$/, "");
    const extensions = ["png", "jpg", "jpeg", "webp", "svg"];
    const folders = ["", "images", "img"];

    const candidates = [];
    // Exact file first
    folders.forEach((f) => candidates.push(f ? `${f}/${fileName}` : fileName));
    // Case variations with all extensions
    folders.forEach((f) => {
      extensions.forEach((ext) => {
        candidates.push(f ? `${f}/${baseName}.${ext}` : `${baseName}.${ext}`);
        candidates.push(f ? `${f}/${baseName.toLowerCase()}.${ext}` : `${baseName.toLowerCase()}.${ext}`);
        candidates.push(f ? `${f}/${baseName.toUpperCase()}.${ext}` : `${baseName.toUpperCase()}.${ext}`);
      });
    });
    // Deduplicate
    const unique = [...new Set(candidates)];

    const testNext = (index) => {
      if (index >= unique.length) return; // No image found, placeholder stays
      const src = unique[index];
      const test = new Image();
      test.onload = () => {
        const realImg = document.createElement("img");
        realImg.src = src;
        realImg.alt = baseName;
        slot.classList.add("has-image");
        slot.classList.remove("is-empty");
        slot.appendChild(realImg);
      };
      test.onerror = () => {
        if (index === unique.length - 1) slot.classList.add("is-empty");
        testNext(index + 1);
      };
      test.src = src;
    };

    testNext(0);
  };

  document.querySelectorAll(".media-slot").forEach(loadImageIfExists);

  const experienceCards = Array.from(document.querySelectorAll(".experience-card"));
  const btnShowMore = document.getElementById("show-more-experience");
  const remainingText = document.getElementById("remaining-experience");
  const progressText = document.getElementById("experience-progress");
  const visibleByDefault = 3;

  const updateExperienceCounters = () => {
    const shown = experienceCards.filter((card) => !card.classList.contains("is-hidden")).length;
    const total = experienceCards.length;
    const remaining = Math.max(total - shown, 0);

    if (progressText) progressText.textContent = `Mostrando ${shown} de ${total}`;
    if (remainingText) remainingText.textContent = `${remaining} restantes`;

    if (btnShowMore) {
      btnShowMore.style.display = remaining > 0 ? "inline-flex" : "none";
    }
  };

  experienceCards.forEach((card, index) => {
    if (index >= visibleByDefault) card.classList.add("is-hidden");
  });

  if (btnShowMore) {
    btnShowMore.addEventListener("click", () => {
      const next = experienceCards.find((card) => card.classList.contains("is-hidden"));
      if (!next) return;

      next.classList.remove("is-hidden");
      next.classList.add("is-reveal");
      setTimeout(() => next.classList.remove("is-reveal"), 520);

      updateExperienceCounters();
    });
  }

  updateExperienceCounters();
});
