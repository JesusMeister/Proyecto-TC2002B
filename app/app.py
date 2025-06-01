# app.py
import streamlit as st

# Importar módulos de página y configuración
from full_pages import platform_analysis
from full_pages import polarization_cohesion_metrics
from styling import apply_global_styles
from full_pages import home
from components.ui_elements import app_footer

# Aplicar estilos globales y configuración de página una vez
apply_global_styles()

def main():

    if 'current_page' not in st.session_state:
        st.session_state.current_page = "🏠 Página de Inicio"

    page_options = ["🏠 Página de Inicio", "📊 Análisis de Plataformas", "📈 Análisis de Cohesión y Polarización"]

    # Cambiar a barra lateral:
    page = st.sidebar.radio(
        "Selecciona una sección:",
        options=page_options,
        index=page_options.index(st.session_state.current_page), # Para recordar la selección
        label_visibility="visible"
    )
    st.session_state.current_page = page  # Actualizar estado

    # Renderizar la página seleccionada
    if page == "🏠 Página de Inicio":
        home.show_page()
    elif page == "📊 Análisis de Plataformas":
        platform_analysis.show_page()
    elif page == "📈 Análisis de Cohesión y Polarización":
        polarization_cohesion_metrics.show_page()

    # Footer común a todas las páginas
    app_footer()

if __name__ == "__main__":
    main()