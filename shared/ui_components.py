"""Componentes UI reutilizables para mantener consistencia visual."""

import streamlit as st

EXECUTIVE_HEADER_GRADIENT = "linear-gradient(125deg, #0F172A 0%, #0E7490 66%, #1E3A8A 100%)"


def inject_sidebar_navigation_styles() -> None:
    """Inyecta el sistema visual global (tipografía, paleta, sidebar y componentes base)."""
    st.markdown(
        """
        <style>
        @import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap");

        :root {
            --bg-main: #F8FAFC;
            --bg-section: #F1F5F9;
            --bg-card: #FFFFFF;
            --accent: #0E7490;
            --text-primary: #0F172A;
            --text-secondary: #475569;
            --border-soft: #CBD5E1;
            --font-sans: "Inter", "Source Sans 3", "Segoe UI", "Roboto", "Arial", sans-serif;
            --font-mono: "JetBrains Mono", "Source Code Pro", "Consolas", monospace;
            --shadow-soft: 0 8px 22px rgba(15, 23, 42, 0.08);
        }

        html, body, [data-testid="stAppViewContainer"], .stApp {
            font-family: var(--font-sans);
            background: var(--bg-main);
            color: var(--text-primary);
        }

        [data-testid="stMainBlockContainer"] {
            max-width: 1160px;
            padding-top: 1.45rem;
            padding-bottom: 2.4rem;
        }

        h1, h2, h3, h4, h5, h6,
        p, li, label, input, textarea, select, button,
        [data-testid="stMarkdownContainer"] {
            font-family: var(--font-sans) !important;
        }

        h1, h2, h3 {
            color: var(--text-primary);
            letter-spacing: -0.01em;
        }

        [data-testid="stMarkdownContainer"] p,
        [data-testid="stMarkdownContainer"] li {
            color: var(--text-secondary);
            line-height: 1.62;
            font-size: 1rem;
        }

        hr {
            border-top: 1px solid var(--border-soft) !important;
        }

        .app-hero {
            color: #FFFFFF;
            border-radius: 18px;
            padding: 2.55rem 2rem;
            border: 1px solid rgba(255, 255, 255, 0.24);
            box-shadow: 0 14px 34px rgba(15, 23, 42, 0.24);
            margin-bottom: 1.65rem;
            text-align: center;
        }

        .app-hero h1 {
            margin: 0 0 0.6rem 0;
            font-size: clamp(2rem, 2.8vw, 2.6rem);
            font-weight: 900;
            color: #FFFFFF;
        }

        .app-hero p {
            margin: 0;
            color: #CBD5E1;
            font-size: 1rem;
            font-weight: 500;
        }

        .quick-link-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.85rem;
            margin: 0.45rem 0 0.25rem;
        }

        .quick-link-btn {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            min-height: 46px;
            width: 100%;
            border-radius: 10px;
            border: 1px solid var(--border-soft);
            background: var(--bg-card);
            color: var(--text-primary) !important;
            text-decoration: none !important;
            font-weight: 650;
            font-size: 0.95rem;
            transition: all 0.2s ease;
        }

        .quick-link-btn:hover {
            border-color: var(--accent);
            box-shadow: 0 5px 16px rgba(14, 116, 144, 0.16);
            transform: translateY(-1px);
        }

        [data-testid="metric-container"] {
            background: var(--bg-card);
            border: 1px solid var(--border-soft);
            border-left: 4px solid var(--accent);
            border-radius: 12px;
            padding: 0.7rem 0.85rem;
            box-shadow: var(--shadow-soft);
            min-height: 122px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            text-align: center;
        }

        [data-testid="metric-container"] > div {
            width: 100%;
            text-align: center;
        }

        [data-testid="metric-container"] [data-testid="stMetricLabel"] {
            justify-content: center !important;
        }

        [data-testid="metric-container"] label {
            color: var(--text-secondary) !important;
            font-size: 0.82rem !important;
            letter-spacing: 0.03em;
            text-transform: uppercase;
            font-weight: 700 !important;
        }

        [data-testid="metric-container"] [data-testid="stMetricValue"] {
            font-family: var(--font-mono);
            color: var(--text-primary);
            font-weight: 700;
            justify-content: center !important;
            text-align: center;
            font-size: clamp(1.45rem, 2.3vw, 1.9rem);
        }

        [data-testid="stSidebar"] {
            background: #F1F5F9;
            border-right: 1px solid var(--border-soft);
        }

        [data-testid="stSidebarContent"] {
            padding-top: 0.2rem;
        }

        [data-testid="stSidebarNav"] {
            padding-top: 0.65rem;
        }

        [data-testid="stSidebarNav"] ul {
            gap: 0.22rem;
        }

        [data-testid="stSidebarNav"] ul li a {
            border-radius: 9px;
            padding: 0.5rem 0.7rem;
            border-left: 3px solid transparent;
            transition: all 0.2s ease;
        }

        [data-testid="stSidebarNav"] ul li a p,
        [data-testid="stSidebarNav"] ul li a span {
            color: var(--text-secondary) !important;
            font-size: 1.02rem !important;
            font-weight: 600 !important;
            line-height: 1.3 !important;
        }

        [data-testid="stSidebarNav"] ul li a:hover {
            background: #CBD5E1;
            border-left-color: #1E3A8A;
        }

        [data-testid="stSidebarNav"] ul li a:focus-visible {
            outline: 2px solid var(--accent);
            outline-offset: 2px;
        }

        [data-testid="stSidebarNav"] ul li a[aria-current="page"] {
            background: #CBD5E1;
            border-left-color: var(--accent);
            box-shadow: inset 0 0 0 1px rgba(14, 116, 144, 0.22);
        }

        [data-testid="stSidebarNav"] ul li a[aria-current="page"] p,
        [data-testid="stSidebarNav"] ul li a[aria-current="page"] span {
            color: var(--text-primary) !important;
            font-weight: 750 !important;
        }

        div[data-testid="stForm"] {
            border: 1px solid var(--border-soft);
            border-radius: 14px;
            padding: 1rem;
            background: var(--bg-card);
            box-shadow: var(--shadow-soft);
        }

        .stTextInput > div > div > input,
        .stTextArea textarea,
        .stSelectbox [data-baseweb="select"] > div {
            border-radius: 10px !important;
            border: 1px solid var(--border-soft) !important;
        }

        .stButton > button,
        [data-testid="stFormSubmitButton"] button {
            border-radius: 10px !important;
            border: 1px solid var(--accent) !important;
            background: var(--accent) !important;
            color: #FFFFFF !important;
            font-weight: 700 !important;
        }

        .stButton > button:hover,
        [data-testid="stFormSubmitButton"] button:hover {
            background: #1E3A8A !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_page_header(title: str, subtitle: str, gradient: str) -> None:
    inject_sidebar_navigation_styles()
    st.markdown(
        f"""
        <div class="app-hero" style="background: {gradient};">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_quick_links(correo: str, telefono: str, linkedin_url: str) -> None:
    linkedin_display = linkedin_url.replace("https://", "").replace("http://", "").replace("www.", "")
    st.markdown(
        f"""
        <div class="quick-link-grid">
            <a class="quick-link-btn" href="mailto:{correo}">📧 Enviar Email</a>
            <a class="quick-link-btn" href="{linkedin_url}" target="_blank" rel="noopener noreferrer">{linkedin_display} ↗</a>
            <a class="quick-link-btn" href="tel:{telefono}">📞 Llamar</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
