# Importamos las librerías necesarias
import streamlit as st
from pathlib import Path
import os

# Determinar la ruta base para los plots individuales
current_script_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_script_dir, os.pardir) # Esto debería ser 'app/'
BASE_PLOT_PATH = Path(os.path.join(parent_dir, "static", "plots", "individual"))

# Constantes para los nombres de archivo de los plots
NETWORK_PLOT_FILENAME = "network.html" # Asumiendo este nombre para la red
DENSITY_PLOT_FILENAME = "density.html"      # Basado en tu ejemplo de ruta

# Función que genera la barra lateral del dashboard
def render_sidebar(base_plot_path):
    """
    Genera la barra lateral para la selección de categoría y usuario.
    """
    with st.sidebar:
        st.markdown("### 🗂️ Panel de Control Individual")
        st.markdown("---")

        # 1. Selector de Categorías
        st.markdown("**Selecciona una categoría:**")
        try:
            # Listar directorios que no comiencen con '.'
            categories = sorted([
                d.name for d in base_plot_path.iterdir()
                if d.is_dir() and not d.name.startswith('.')
            ])
        except Exception as e:
            st.error(f"❌ Error al cargar categorías: {e}")
            return None, None

        if not categories:
            st.warning("⚠️ No se encontraron categorías en la carpeta de datos.")
            st.info(f"📁 Estructura esperada: `{base_plot_path}/[nombre_categoria]/`")
            return None, None

        selected_category = st.selectbox(
            "Categorías disponibles",
            categories,
            help="Elige la categoría que deseas analizar",
            key="individual_category_selector"
        )

        selected_user = None
        users_in_category = 0
        if selected_category:
            category_path = base_plot_path / selected_category
            if not category_path.exists() or not category_path.is_dir():
                st.warning(f"⚠️ La carpeta para la categoría '{selected_category}' no existe.")
                return selected_category, None

            st.markdown("**Selecciona un usuario:**")
            try:
                users = sorted([
                    d.name for d in category_path.iterdir()
                    if d.is_dir() and not d.name.startswith('.')
                ])
                users_in_category = len(users)
            except Exception as e:
                st.error(f"❌ Error al cargar usuarios para '{selected_category}': {e}")
                return selected_category, None

            if not users:
                st.warning(f"⚠️ No se encontraron usuarios en la categoría '{selected_category}'.")
                st.info(f"📁 Estructura esperada: `{category_path}/[nombre_usuario]/`")
                return selected_category, None

            selected_user = st.selectbox(
                "Usuarios disponibles",
                users,
                help="Elige el usuario que deseas analizar",
                key="individual_user_selector"
            )

        st.markdown("---")
        st.markdown("### 📊 Información")
        st.info(f"**{len(categories)}** categorías disponibles.")
        if selected_category:
            st.info(f"**{users_in_category}** usuarios en '{selected_category}'.")

        st.markdown("### 💡 Ayuda")
        with st.expander("¿Cómo usar el dashboard?"):
            st.markdown("""
            1. **Selecciona** una categoría del menú.
            2. **Selecciona** un usuario de la lista.
            3. **Explora** las pestañas para ver la red y el análisis de densidad del usuario.
            """)
    return selected_category, selected_user


# Función principal que muestra la página
def show_page():
    """Dashboard de análisis individual de usuarios"""

    st.markdown("""
        <h1 class="main-title">
            📊 Dashboard de Análisis Individual de Usuarios
        </h1>
        <p style="text-align: center; color: var(--text-secondary); font-size: 1.1rem; margin-bottom: 2rem;">
            Explora la actividad y conexiones de usuarios específicos en cada categoría
        </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Validación de existencia de la carpeta de datos principal
    if not BASE_PLOT_PATH.exists():
        st.error(f"❌ No se encontró la carpeta de datos para análisis individuales. Asegúrate de que existe: `{BASE_PLOT_PATH}`")
        st.info(f"📁 Estructura esperada: `{BASE_PLOT_PATH}/[nombre_categoria]/[nombre_usuario]/`")
        return

    # Mostramos la barra lateral y obtenemos la categoría y usuario seleccionados
    selected_category, selected_user = render_sidebar(BASE_PLOT_PATH)

    if selected_category and selected_user:
        st.markdown(f"## Análisis de: **{selected_user}** (Categoría: *{selected_category}*)")
        st.markdown("---")

        user_folder_path = BASE_PLOT_PATH / selected_category / selected_user

        if not user_folder_path.exists() or not user_folder_path.is_dir():
            st.error(f"❌ No se encontró la carpeta para el usuario '{selected_user}' en la categoría '{selected_category}'.")
            st.info(f"📁 Verifica la ruta: `{user_folder_path}`")
            return

        # Pestañas para diferentes análisis
        tab1, tab2 = st.tabs([
            "🌐 Red de Usuario",
            "📈 Análisis de Densidad"
        ])

        # TAB 1: Visualización de la red del usuario
        with tab1:
            st.markdown('<p class="section-header">Red de Conexiones del Usuario</p>', unsafe_allow_html=True)
            network_file = user_folder_path / NETWORK_PLOT_FILENAME
            if network_file.exists():
                try:
                    with open(network_file, 'r', encoding='utf-8') as f:
                        html_network = f.read()
                    st.markdown("""
                        <div class="info-card">
                            <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                                Esta visualización muestra las conexiones del usuario seleccionado basadas en similitud discursiva.
                                Los nodos representan otros usuarios y las conexiones indican similitudes en el contenido.
                            </p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.components.v1.html(html_network, height=650, scrolling=True)
                except Exception as e:
                    st.error(f"❌ Error al cargar la visualización de red: {e}")
            else:
                st.warning(f"⚠️ Visualización de red no disponible para '{selected_user}'.")
                st.info(f"💡 Genera el archivo `{NETWORK_PLOT_FILENAME}` en `{user_folder_path}` para ver esta visualización.")

        # TAB 2: Visualización del análisis de densidad del usuario
        with tab2:
            st.markdown('<p class="section-header">Análisis de Densidad del Usuario</p>', unsafe_allow_html=True)
            density_file = user_folder_path / DENSITY_PLOT_FILENAME
            if density_file.exists():
                try:
                    with open(density_file, 'r', encoding='utf-8') as f:
                        html_density = f.read()
                    st.markdown("""
                        <div class="info-card">
                            <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                                El análisis de densidad muestra la distribución espacial del usuario seleccionado y 
                                la concentración de su actividad en diferentes regiones de la red.
                            </p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.components.v1.html(html_density, height=650, scrolling=True)
                except Exception as e:
                    st.error(f"❌ Error al cargar la visualización de densidad: {e}")
            else:
                st.warning(f"📊 Análisis de densidad no disponible para '{selected_user}'.")
                st.info(f"💡 Genera el archivo `{DENSITY_PLOT_FILENAME}` en `{user_folder_path}` para ver esta visualización.")
    elif selected_category:
        st.info(f"ℹ️ Selecciona un usuario de la categoría '{selected_category}' para ver su análisis.")
    else:
        st.info("ℹ️ Selecciona una categoría y un usuario en el panel de la izquierda para comenzar.")

# Para ejecutar la aplicación, llama a show_page()
if __name__ == "__main__":
    show_page()