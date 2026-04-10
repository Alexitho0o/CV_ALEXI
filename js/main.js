document.addEventListener("DOMContentLoaded", () => {
  document.body.classList.add("has-js");

  const nav = document.querySelector(".navbar");
  const navContainer = document.querySelector(".navbar-container");
  const navLinks = Array.from(document.querySelectorAll(".nav-link"));
  const sections = Array.from(document.querySelectorAll("main section[id]"));
  const navToggle = document.querySelector(".navbar-toggle");
  const navMenu = document.querySelector(".nav-menu");
  const mediaResizeObservers = new WeakMap();
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const getNavOffset = () => (nav ? nav.offsetHeight + 14 : 90);
  const closeMenu = ({ focusToggle = false } = {}) => {
    if (!navMenu || !navToggle) return;
    navMenu.classList.remove("open");
    navToggle.setAttribute("aria-expanded", "false");
    if (focusToggle) navToggle.focus();
  };

  const setMenuOpen = (isOpen) => {
    if (!navMenu || !navToggle) return;
    navMenu.classList.toggle("open", isOpen);
    navToggle.setAttribute("aria-expanded", String(isOpen));
  };

  const isInsideToggleHitArea = (event) => {
    if (!navToggle || typeof event.clientX !== "number" || typeof event.clientY !== "number") return false;
    const rect = navToggle.getBoundingClientRect();
    return (
      event.clientX >= rect.left &&
      event.clientX <= rect.right &&
      event.clientY >= rect.top &&
      event.clientY <= rect.bottom
    );
  };

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", (event) => {
      event.stopPropagation();
      setMenuOpen(!navMenu.classList.contains("open"));
    });

    if (navContainer) {
      navContainer.addEventListener("click", (event) => {
        if (event.target.closest(".navbar-toggle")) return;
        if (!isInsideToggleHitArea(event)) return;
        event.preventDefault();
        event.stopPropagation();
        setMenuOpen(!navMenu.classList.contains("open"));
      });
    }

    document.addEventListener("click", (event) => {
      if (!navMenu.classList.contains("open")) return;
      if (nav.contains(event.target)) return;
      closeMenu();
    });

    document.addEventListener("keydown", (event) => {
      if (event.key !== "Escape" || !navMenu.classList.contains("open")) return;
      closeMenu({ focusToggle: true });
    });

    window.addEventListener("resize", () => {
      if (window.innerWidth > 840) closeMenu();
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
      window.scrollTo({ top: Math.max(top, 0), behavior: prefersReducedMotion ? "auto" : "smooth" });

      if (!target.hasAttribute("tabindex")) {
        target.setAttribute("tabindex", "-1");
      }
      target.focus({ preventScroll: true });

      closeMenu();
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
      const isActive = link.getAttribute("href") === `#${current}`;
      link.classList.toggle("active", isActive);
      if (isActive) {
        link.setAttribute("aria-current", "location");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  };

  window.addEventListener("scroll", setActiveLink, { passive: true });
  setActiveLink();

  const revealTargets = document.querySelectorAll(".section, .experience-card, .media-slot");
  revealTargets.forEach((el) => el.classList.add("reveal"));

  if (prefersReducedMotion || !("IntersectionObserver" in window)) {
    revealTargets.forEach((el) => el.classList.add("in-view"));
  } else {
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
  }

  function updateMediaSlot(slot) {
    const img = slot.querySelector("img");
    if (!img) {
      slot.classList.add("is-empty");
      slot.classList.remove("has-image");
      return;
    }

    if (!img.naturalWidth || !img.naturalHeight) return;

    const slotW = slot.clientWidth;
    const slotH = slot.clientHeight;
    if (!slotW || !slotH) return;

    const ir = img.naturalWidth / img.naturalHeight;
    const sr = slotW / slotH;
    const mismatch = Math.max(ir / sr, sr / ir);

    slot.style.setProperty("--fx", (slot.dataset.fx || 50) + "%");
    slot.style.setProperty("--fy", (slot.dataset.fy || 50) + "%");

    if (mismatch > 1.8) {
      slot.dataset.mode = "padded";
      slot.style.setProperty("--bg-image", `url("${img.currentSrc || img.src}")`);
    } else {
      slot.dataset.mode = "cover";
      slot.style.setProperty("--bg-image", "none");
    }

    slot.classList.add("has-image");
    slot.classList.remove("is-empty");
  }

  function initMediaSlots() {
    document.querySelectorAll(".media-slot").forEach((slot) => {
      const img = slot.querySelector("img");

      if (!img) {
        slot.classList.add("is-empty");
        slot.classList.remove("has-image");
        return;
      }

      const run = () => updateMediaSlot(slot);

      if (img.complete && img.naturalWidth) {
        run();
      } else {
        img.addEventListener("load", run, { once: true });
        img.addEventListener(
          "error",
          () => {
            slot.classList.add("is-empty");
            slot.classList.remove("has-image");
          },
          { once: true }
        );
      }

      if ("ResizeObserver" in window) {
        const ro = new ResizeObserver(run);
        ro.observe(slot);
      } else {
        window.addEventListener("resize", run);
      }
    });
  }

  initMediaSlots();

  const ensureMediaSlotObserver = (slot, run) => {
    if (mediaResizeObservers.has(slot)) return;

    if ("ResizeObserver" in window) {
      const ro = new ResizeObserver(run);
      ro.observe(slot);
      mediaResizeObservers.set(slot, ro);
    } else {
      window.addEventListener("resize", run);
      mediaResizeObservers.set(slot, true);
    }
  };

  const bindImageToSlot = (slot, img) => {
    const run = () => updateMediaSlot(slot);

    img.addEventListener(
      "load",
      () => {
        slot.classList.add("has-image");
        slot.classList.remove("is-empty");
        run();
      },
      { once: true }
    );

    img.addEventListener(
      "error",
      () => {
        slot.classList.add("is-empty");
        slot.classList.remove("has-image");
      },
      { once: true }
    );

    if (img.complete && img.naturalWidth) {
      slot.classList.add("has-image");
      slot.classList.remove("is-empty");
      run();
    }

    ensureMediaSlotObserver(slot, run);
  };

  const loadImageIfExists = (slot) => {
    const existingImage = slot.querySelector("img");
    if (existingImage) {
      bindImageToSlot(slot, existingImage);
      return;
    }

    const fileName = slot.getAttribute("data-image-file");
    if (!fileName) {
      slot.classList.add("is-empty");
      return;
    }

    const dotIndex = fileName.lastIndexOf(".");
    const rawBaseName = dotIndex >= 0 ? fileName.slice(0, dotIndex) : fileName;
    const fileBaseName = rawBaseName.split("/").pop() || rawBaseName;
    const extensions = ["png", "jpg", "jpeg", "webp", "svg"];
    const folders = ["", "images", "img"];
    const candidates = [];

    folders.forEach((folder) => {
      const prefix = folder ? `${folder}/` : "";
      candidates.push(`${prefix}${fileName}`);
      extensions.forEach((extension) => {
        candidates.push(`${prefix}${rawBaseName}.${extension}`);
        candidates.push(`${prefix}${rawBaseName.toLowerCase()}.${extension}`);
        candidates.push(`${prefix}${rawBaseName.toUpperCase()}.${extension}`);
      });
    });

    const uniqueCandidates = [...new Set(candidates)];

    const testNext = (index) => {
      if (index >= uniqueCandidates.length) {
        slot.classList.add("is-empty");
        slot.classList.remove("has-image");
        slot.setAttribute("data-error", "Image failed to load");
        return;
      }

      const source = uniqueCandidates[index];
      const probe = new Image();

      probe.onload = () => {
        const realImg = document.createElement("img");
        realImg.src = source;
        realImg.alt = fileBaseName;
        realImg.loading = "lazy";
        realImg.decoding = "async";
        bindImageToSlot(slot, realImg);
        slot.appendChild(realImg);
      };

      probe.onerror = () => {
        testNext(index + 1);
      };

      probe.src = source;
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
      btnShowMore.setAttribute(
        "aria-label",
        remaining > 0 ? "Mostrar una experiencia adicional" : "No hay más experiencias para mostrar"
      );
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
      if (!prefersReducedMotion) {
        next.classList.add("is-reveal");
        setTimeout(() => next.classList.remove("is-reveal"), 520);
      }

      updateExperienceCounters();
    });
  }

  updateExperienceCounters();
});
