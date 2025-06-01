# Importamos las librerías necesarias
import streamlit as st
from pathlib import Path

# Importamos funciones auxiliares desde módulos propios
from utils.helpers import create_platform_metrics 
from components.ui_elements import display_platform_overview

# Definimos la ruta base donde se encuentran los archivos de visualización
BASE_PLOT_PATH = Path("static_data/plots") / "platforms"

# Función que genera la barra lateral del dashboard
def render_sidebar(platforms):
    with st.sidebar:
        # Título del panel
        st.markdown("### 🗂️ Panel de Control")
        st.markdown("---")

        # Selector de plataformas
        st.markdown("**Selecciona una plataforma:**")
        selected_platform = st.selectbox(
            "Plataformas disponibles",
            platforms,
            help="Elige la plataforma que deseas analizar"
        )

        st.markdown("---")

        # Información general
        st.markdown("### 📊 Información")
        st.info(f"**{len(platforms)}** plataformas disponibles")

        # Sección de ayuda desplegable
        st.markdown("### 💡 Ayuda")
        with st.expander("¿Cómo usar el dashboard?"):
            st.markdown("""
            1. **Selecciona** una plataforma del menú
            2. **Explora** las pestañas disponibles
            3. **Analiza** las visualizaciones
            4. **Compara** diferentes clusters
            """)
    return selected_platform


# Función principal que muestra la página
def show_page():
    """Dashboard principal de análisis de plataformas"""

    # Título del dashboard con estilos HTML
    st.markdown("""
        <h1 class="main-title">
            📊 Dashboard de Análisis de Plataformas
        </h1>
        <p style="text-align: center; color: var(--text-secondary); font-size: 1.1rem; margin-bottom: 2rem;">
            Explora las comunidades identificadas en cada plataforma digital
        </p>
    """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Validación de existencia de la carpeta de datos
    if not BASE_PLOT_PATH.exists():
        st.error(f"❌ No se encontró la carpeta de datos. Asegúrate de que existe: `{BASE_PLOT_PATH}`")
        st.info(f"📁 Estructura esperada: `{BASE_PLOT_PATH}/[nombre_plataforma]/`")
        return

    # Cargamos los nombres de las plataformas desde las carpetas
    try:
        platforms = [d.name for d in BASE_PLOT_PATH.iterdir() 
                    if d.is_dir() and not d.name.startswith('.')]

        if not platforms:
            st.warning("⚠️ No se encontraron plataformas en la carpeta de datos.")
            return

    except Exception as e:
        st.error(f"Error al cargar plataformas: {e}")
        return

    # Mostramos la barra lateral y obtenemos la plataforma seleccionada
    selected_platform = render_sidebar(platforms)

    if selected_platform:
        # Ruta a la carpeta específica de la plataforma
        platform_folder = BASE_PLOT_PATH / selected_platform
        metrics = create_platform_metrics(platform_folder)  # Cálculo de métricas

        # Mostramos la información general de la plataforma
        display_platform_overview(selected_platform, metrics)

        # Pestañas para diferentes análisis
        tab1, tab2, tab3 = st.tabs([
            "🌐 Red de Usuarios", 
            "📈 Análisis de Densidad", 
            "🧠 Exploración de Comunidades"
        ])

        # TAB 1: Visualización de la red de usuarios
        with tab1:
            st.markdown('<p class="section-header">Red de Conexiones de Usuarios</p>', unsafe_allow_html=True)
            network_file = platform_folder / "network_plot.html"
            if network_file.exists():
                try:
                    with open(network_file, 'r', encoding='utf-8') as f:
                        html_network = f.read()
                    st.markdown("""
                        <div class="info-card">
                            <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                                Esta visualización muestra las conexiones entre usuarios basadas en similitud discursiva.
                                Los nodos representan usuarios y las conexiones indican similitudes en el contenido.
                            </p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.components.v1.html(html_network, height=650, scrolling=True)
                except Exception as e:
                    st.error(f"Error al cargar la visualización de red: {e}")
            else:
                st.warning("⚠️ Visualización de red no disponible para esta plataforma.")
                st.info("💡 Genera el archivo `network_plot.html` para ver esta visualización.")

        # TAB 2: Visualización del análisis de densidad
        with tab2:
            st.markdown('<p class="section-header">Análisis de Densidad de Usuarios</p>', unsafe_allow_html=True)
            density_file = platform_folder / "density_plot.html"
            if density_file.exists():
                try:
                    with open(density_file, 'r', encoding='utf-8') as f:
                        html_density = f.read()
                    st.markdown("""
                        <div class="info-card">
                            <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                                El análisis de densidad muestra la distribución espacial de usuarios y 
                                la concentración de actividad en diferentes regiones de la red.
                            </p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.components.v1.html(html_density, height=650, scrolling=True)
                except Exception as e:
                    st.error(f"Error al cargar la visualización de densidad: {e}")
            else:
                st.info("📊 Análisis de densidad no disponible para esta plataforma.")
                st.info("💡 Genera el archivo `density_plot.html` para ver esta visualización.")

        # TAB 3: Exploración detallada de comunidades (clusters)
        with tab3:
            st.markdown('<p class="section-header">Exploración Detallada de Comunidades</p>', unsafe_allow_html=True)
            clusters_folder = platform_folder / "clusters"
            if clusters_folder.exists():
                # Obtenemos archivos de clusters disponibles y limpiamos nombres
                cluster_files = sorted([
                    f.name for f in clusters_folder.iterdir()
                    if f.name.startswith("cluster_") and f.name.endswith(".html")
                ])

                # Creamos lista con nombres limpios para mostrar sin prefijo ni extensión
                cluster_names = [f.replace("cluster_", "").replace(".html", "") for f in cluster_files]

                if cluster_files:
                    st.markdown("""
                        <div class="info-card">
                            <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                                Los clusters agrupan usuarios con patrones discursivos similares. 
                                Cada cluster incluye una nube de palabras y visualización interactiva.
                            </p>
                        </div>
                    """, unsafe_allow_html=True)

                    # Selección del cluster por nombre limpio
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        selected_cluster_name = st.selectbox(
                            "Selecciona un cluster para explorar:",
                            cluster_names,
                            help="Cada cluster representa un grupo de usuarios con patrones similares"
                        )
                    with col2:
                        st.metric("Número de Comunidades encontradas", len(cluster_files))

                    if selected_cluster_name:
                        # Construimos el nombre del archivo a partir del nombre limpio seleccionado
                        selected_cluster_file = f"cluster_{selected_cluster_name}.html"
                        cluster_path = clusters_folder / selected_cluster_file
                        wordcloud_file = clusters_folder / f"wordcloud_{selected_cluster_name}.png"

                        # Mostramos la visualización interactiva del cluster
                        st.markdown("#### 📊 Visualización Interactiva de la Comunidad")
                        try:
                            with open(cluster_path, 'r', encoding='utf-8') as f:
                                html_cluster = f.read()
                            st.components.v1.html(html_cluster, height=650, scrolling=True)
                        except Exception as e:
                            st.error(f"Error al cargar la visualización de la Comunidad: {e}")

                        if wordcloud_file.exists():
                            st.markdown("#### 🏷️ Nube de Palabras de la Comunidad")
                            img_col1, img_col2, img_col3 = st.columns([1, 3, 1])
                            with img_col2:
                                st.image(
                                    str(wordcloud_file), 
                                    caption=f"Términos más relevantes - Comunidad {selected_cluster_name}",
                                )
                else:
                    st.warning("⚠️ No se encontraron archivos de clusters para esta plataforma.")
                    st.info("💡 Genera los archivos de clusters para explorar esta funcionalidad.")
            else:
                st.warning("📁 No existe la carpeta de clusters para esta plataforma.")
                st.info(f"💡 Crea la estructura: `{BASE_PLOT_PATH}/[plataforma]/clusters/`")