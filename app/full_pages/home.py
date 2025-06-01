# pages/home.py
import streamlit as st

def show_page():
    """Página de inicio del proyecto"""

    # Hero section
    st.markdown("""
        <div style="text-align: center; padding-top: 0rem; padding-bottom: 3rem;">
            <h1 class="main-title" style="font-size: 3.5rem; margin-bottom: 1rem;">
                🌐 Inferencia de Comunidades<br>en Redes Sociales
            </h1>
            <p style="font-size: 1.3rem; color: var(--text-secondary); max-width: 800px; margin: 0 auto 2rem auto; line-height: 1.6;">
                Análisis avanzado de patrones discursivos para identificar comunidades de usuarios en plataformas digitales
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Sección principal del proyecto
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
            <div class="info-card" style="margin-bottom: 2rem;">
                <h2 style="color: var(--primary-blue); margin-bottom: 1.5rem; font-size: 1.8rem;">
                    📋 Resumen del Proyecto
                </h2>
                <p style="font-size: 1.1rem; line-height: 1.7; color: var(--text-primary); margin-bottom: 1.5rem;">
                    Este proyecto implementa técnicas avanzadas de <strong>análisis de redes sociales</strong> y 
                    <strong>procesamiento de lenguaje natural</strong> para identificar comunidades de usuarios 
                    basándose en la <strong>similitud discursiva</strong> de sus contenidos.
                </p>
                <p style="font-size: 1.1rem; line-height: 1.7; color: var(--text-primary);">
                    A través del análisis del lenguaje utilizado por los usuarios, el sistema es capaz de 
                    detectar patrones, agrupar usuarios con intereses similares y visualizar la estructura 
                    de comunidades que emergen naturalmente en las plataformas digitales.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="info-card" style="background: linear-gradient(135deg, var(--light-blue), #f0f7ff); border-left: 4px solid var(--primary-blue);">
                <h3 style="color: var(--primary-blue); margin-bottom: 1rem;">🎯 Objetivos Clave</h3>
                <ul style="list-style: none; padding: 0; margin: 0;">
                    <li style="margin-bottom: 0.8rem; padding-left: 1.5rem; position: relative;">
                        <span style="position: absolute; left: 0; color: var(--primary-blue);">🔍</span>
                        Identificar comunidades naturales
                    </li>
                    <li style="margin-bottom: 0.8rem; padding-left: 1.5rem; position: relative;">
                        <span style="position: absolute; left: 0; color: var(--primary-blue);">📊</span>
                        Visualizar patrones discursivos
                    </li>
                    <li style="margin-bottom: 0.8rem; padding-left: 1.5rem; position: relative;">
                        <span style="position: absolute; left: 0; color: var(--primary-blue);">🌐</span>
                        Mapear conexiones entre usuarios
                    </li>
                    <li style="margin-bottom: 0.8rem; padding-left: 1.5rem; position: relative;">
                        <span style="position: absolute; left: 0; color: var(--primary-blue);">💡</span>
                        Generar insights actionables
                    </li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # Metodología
    st.markdown("""
        <div class="info-card" style="margin: 2rem 0;">
            <h2 style="color: var(--primary-blue); margin-bottom: 1.5rem; font-size: 1.8rem;">
                🔬 Metodología de Análisis
            </h2>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="metric-card" style="height: 200px; display: flex; flex-direction: column; justify-content: center;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">📝</div>
                <h4 style="color: var(--primary-blue); margin-bottom: 1rem;">Procesamiento de Texto</h4>
                <p style="font-size: 0.9rem; color: var(--text-secondary);">
                    Análisis semántico y extracción de características discursivas del contenido generado por usuarios
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="metric-card" style="height: 200px; display: flex; flex-direction: column; justify-content: center;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🔗</div>
                <h4 style="color: var(--primary-blue); margin-bottom: 1rem;">Construcción de Redes</h4>
                <p style="font-size: 0.9rem; color: var(--text-secondary);">
                    Creación de grafos basados en similitud discursiva entre usuarios para mapear conexiones
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="metric-card" style="height: 200px; display: flex; flex-direction: column; justify-content: center;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🎯</div>
                <h4 style="color: var(--primary-blue); margin-bottom: 1rem;">Detección de Comunidades</h4>
                <p style="font-size: 0.9rem; color: var(--text-secondary);">
                    Aplicación de algoritmos de clustering para identificar grupos cohesivos de usuarios
                </p>
            </div>
        """, unsafe_allow_html=True)

    # Características del dashboard
    st.markdown("""
        <div class="info-card" style="margin: 2rem 0;">
            <h2 style="color: var(--primary-blue); margin-bottom: 1.5rem; font-size: 1.8rem;">
                📊 Características del Dashboard
            </h2>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div style="background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border-left: 4px solid #10b981; margin-bottom: 1rem;">
                <h4 style="color: #059669; margin-bottom: 1rem;">🌐 Visualización de Redes</h4>
                <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                    Grafos interactivos que muestran las conexiones entre usuarios basadas en similitud discursiva
                </p>
                <ul style="color: var(--text-secondary); font-size: 0.9rem;">
                    <li>Nodos representan usuarios individuales</li>
                    <li>Aristas indican similitud en el contenido</li>
                    <li>Colores distinguen diferentes comunidades</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div style="background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border-left: 4px solid #f59e0b; margin-bottom: 1rem;">
                <h4 style="color: #d97706; margin-bottom: 1rem;">🧠 Análisis de Comunidades</h4>
                <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                    Exploración detallada de cada comunidad identificada con métricas específicas
                </p>
                <ul style="color: var(--text-secondary); font-size: 0.9rem;">
                    <li>Nubes de palabras por cluster</li>
                    <li>Visualizaciones interactivas por grupo</li>
                    <li>Análisis de términos más relevantes</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border-left: 4px solid #8b5cf6; margin-bottom: 1rem;">
                <h4 style="color: #7c3aed; margin-bottom: 1rem;">📈 Análisis de Densidad</h4>
                <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                    Mapas de calor que muestran la concentración y distribución de usuarios
                </p>
                <ul style="color: var(--text-secondary); font-size: 0.9rem;">
                    <li>Identificación de áreas de alta actividad</li>
                    <li>Patrones de distribución espacial</li>
                    <li>Zonas de intersección entre comunidades</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div style="background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border-left: 4px solid #ef4444; margin-bottom: 1rem;">
                <h4 style="color: #dc2626; margin-bottom: 1rem;">🔍 Exploración Interactiva</h4>
                <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                    Herramientas para navegación y análisis profundo de los resultados
                </p>
                <ul style="color: var(--text-secondary); font-size: 0.9rem;">
                    <li>Selección de plataformas específicas</li>
                    <li>Comparación entre diferentes clusters</li>
                    <li>Métricas en tiempo real del análisis</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # Call to action
    st.markdown("""
        <div style="text-align: center; margin: 3rem 0; padding: 2rem; background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue)); border-radius: 12px; color: white;">
            <h3 style="margin-bottom: 1rem; color: white;">🚀 ¡Explora los Resultados!</h3>
            <p style="font-size: 1.1rem; margin-bottom: 1.5rem; opacity: 0.9;">
                Navega a la sección de <strong>Análisis de Plataformas</strong> para comenzar a explorar 
                las comunidades identificadas en cada red social
            </p>
        </div>
    """, unsafe_allow_html=True)