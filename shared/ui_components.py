"""Componentes UI reutilizables para mantener consistencia visual."""

import streamlit as st


def render_page_header(title: str, subtitle: str, gradient: str) -> None:
    st.markdown(
        f"""
        <div style="background: {gradient}; color: white; padding: 3rem 2rem; border-radius: 16px; margin-bottom: 2rem; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_quick_links(correo: str, telefono: str, linkedin_url: str) -> None:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <a href="mailto:{correo}" style="text-decoration: none;">
                <button style="width: 100%; padding: 0.75rem; background: #0891b2; color: white; border: none; border-radius: 8px; font-weight: 600; cursor: pointer;">
                    📧 Enviar Email
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <a href="{linkedin_url}" target="_blank" style="text-decoration: none;">
                <button style="width: 100%; padding: 0.75rem; background: #0891b2; color: white; border: none; border-radius: 8px; font-weight: 600; cursor: pointer;">
                    💼 LinkedIn
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <a href="tel:{telefono}" style="text-decoration: none;">
                <button style="width: 100%; padding: 0.75rem; background: #0891b2; color: white; border: none; border-radius: 8px; font-weight: 600; cursor: pointer;">
                    📞 Llamar
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )

