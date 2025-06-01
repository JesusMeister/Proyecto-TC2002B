import streamlit as st
from pathlib import Path

# Definimos las rutas base donde se encuentran los archivos de visualización
BASE_POLARIZATION_PATH = Path("static_data/plots/polarization") 
BASE_COHESION_PATH = Path("static_data/plots/cohesion")

def get_available_categories(polarization_path: Path, cohesion_path: Path) -> list[str]:
    """
    Obtiene una lista de categorías (nombres de archivo sin extensión)
    que existen tanto en la carpeta de polarización como en la de cohesión.
    """
    if not polarization_path.exists() or not polarization_path.is_dir():
        st.warning(f"⚠️ La carpeta de gráficos de polarización no existe: {polarization_path}")
        return []
    if not cohesion_path.exists() or not cohesion_path.is_dir():
        st.warning(f"⚠️ La carpeta de gráficos de cohesión no existe: {cohesion_path}")
        return []

    polarization_files = {p.stem for p in polarization_path.glob("*.html") if p.is_file()}
    cohesion_files = {c.stem for c in cohesion_path.glob("*.html") if c.is_file()}

    common_categories = sorted(list(polarization_files.intersection(cohesion_files)))
    return common_categories

def display_html_file(file_path: Path, height: int = 650):
    """Lee y muestra un archivo HTML en Streamlit."""
    if file_path.exists():
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=height, scrolling=True)
        except Exception as e:
            st.error(f"❌ Error al cargar el archivo HTML '{file_path.name}': {e}")
    else:
        st.warning(f"⚠️ El archivo de visualización '{file_path.name}' no fue encontrado en la ruta esperada: {file_path}")

def render_sidebar(categories: list[str]) -> str | None:
    """
    Renderiza la barra lateral con la selección de categoría y la sección de ayuda.
    Retorna la categoría seleccionada o None si no hay categorías.
    """
    with st.sidebar:
        st.markdown("### 🗂️ Panel de Control")
        st.markdown("---")

        if not categories:
            st.warning("⚠️ No hay categorías disponibles para seleccionar.")
            selected_category = None
        else:
            st.markdown("**Selecciona una categoría:**")
            selected_category = st.selectbox(
                "Categorías disponibles",
                options=categories,
                format_func=lambda x: x.replace("_", " ").capitalize(),
                help="Elige la categoría para la cual deseas ver las métricas."
            )
        
        st.markdown("---")

        st.markdown("### 📊 Información")
        st.info(f"**{len(categories)}** categorías disponibles con métricas de polarización y cohesión.")

        st.markdown("---")

        st.markdown("### 💡 Ayuda")
        with st.expander("¿Cómo usar esta aplicación?"):
            st.markdown("""
            1. **Selecciona** una categoría del menú desplegable en la barra lateral.
            2. **Explora** los gráficos de Polarización y Cohesión que se mostrarán en la página principal.
            3. Las visualizaciones te permitirán analizar las métricas para la categoría elegida.
            """)
    
    return selected_category

def show_page():
    """Página para mostrar métricas de Polarización y Cohesión."""

    st.markdown("""
        <h1 class="main-title" style="margin-top: 0rem;">
            ⚖️ Métricas de Polarización y Cohesión
        </h1>
        <p style="text-align: center; color: var(--text-secondary); font-size: 1.1rem; margin-bottom: 2rem;">
            Analiza y compara las métricas de polarización y cohesión para diferentes categorías.
        </p>
    """, unsafe_allow_html=True)

    # Verificar existencia de las carpetas base principales
    if not BASE_POLARIZATION_PATH.exists() and not BASE_COHESION_PATH.exists():
        st.error(f"❌ No se encontraron las carpetas base para los gráficos: '{BASE_POLARIZATION_PATH}' y '{BASE_COHESION_PATH}'.")
        st.info("Asegúrate de que estas carpetas existan y contengan los archivos HTML necesarios.")
        return
    elif not BASE_POLARIZATION_PATH.exists():
        st.error(f"❌ No se encontró la carpeta de gráficos de polarización: '{BASE_POLARIZATION_PATH}'.")
        st.info("Crea esta carpeta y añade los archivos HTML de polarización (ej: medios.html, partidos.html).")
        return
    elif not BASE_COHESION_PATH.exists():
        st.error(f"❌ No se encontró la carpeta de gráficos de cohesión: '{BASE_COHESION_PATH}'.")
        st.info("Crea esta carpeta y añade los archivos HTML de cohesión (ej: medios.html, partidos.html).")
        return

    available_categories = get_available_categories(BASE_POLARIZATION_PATH, BASE_COHESION_PATH)

    if not available_categories:
        st.warning("⚠️ No se encontraron categorías comunes con métricas de polarización y cohesión.")
        st.info(
            f"Asegúrate de que existan archivos HTML con nombres idénticos (ej: 'medios.html') "
            f"en ambas carpetas: '{BASE_POLARIZATION_PATH}' y '{BASE_COHESION_PATH}'."
        )
        return

    # Renderizar la barra lateral y obtener la categoría seleccionada
    selected_category = render_sidebar(available_categories)

    if selected_category:
        st.markdown("---")
        st.markdown(f"""
            <h2 style='text-align: center; color: var(--primary-blue); margin-bottom: 1.5rem; font-size: 1.8rem;'>
                Análisis para: {selected_category.replace("_", " ").capitalize()}
            </h2>
        """, unsafe_allow_html=True)

        # Sección de Polarización
        st.markdown("""
            <div class="info-card" style="margin-bottom: 1rem;">
                <h3 style="color: var(--primary-blue); font-size: 1.5rem;">🔥 Métricas de Polarización</h3>
            </div>
        """, unsafe_allow_html=True)
        polarization_plot_file = BASE_POLARIZATION_PATH / f"{selected_category}.html"
        st.markdown(f"""
            <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                Visualización de las métricas de polarización para la categoría seleccionada.
            </p>
        """, unsafe_allow_html=True)
        display_html_file(polarization_plot_file)

        st.markdown("---")

        # Sección de Cohesión
        st.markdown("""
            <div class="info-card" style="margin-bottom: 1rem; margin-top: 2rem;">
                <h3 style="color: var(--primary-blue); font-size: 1.5rem;">🤝 Métricas de Cohesión</h3>
            </div>
        """, unsafe_allow_html=True)
        cohesion_plot_file = BASE_COHESION_PATH / f"{selected_category}.html"
        st.markdown(f"""
            <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                Visualización de las métricas de cohesión para la categoría seleccionada.
            </p>
        """, unsafe_allow_html=True)
        display_html_file(cohesion_plot_file)

    else:
        st.info("ℹ️ Selecciona una categoría de la barra lateral para ver las métricas.")

# Para ejecutar la aplicación, llama a show_page()
if __name__ == "__main__":
    show_page()