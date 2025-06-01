# styling.py
import streamlit as st

def apply_global_styles():
    st.set_page_config(
        layout="wide",
        page_title="Inferencia de Comunidades en Redes Sociales",
        page_icon="🌐",
        initial_sidebar_state="expanded"
    )

    # Estilos CSS modernos y elegantes
    st.markdown("""
        <style>
            /* Importar fuente moderna */
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

            /* Variables CSS para colores consistentes */
            :root {
                --primary-blue: #2563eb;
                --secondary-blue: #3b82f6;
                --light-blue: #dbeafe;
                --dark-blue: #1e40af;
                --background: #f8fafc;
                --card-bg: #ffffff;
                --text-primary: #1e293b;
                --text-secondary: #64748b;
                --border-color: #e2e8f0;
            }

            /* Estilos generales */
            .main {
                background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
                font-family: 'Inter', sans-serif;
            }

            /* Título principal mejorado */
            .main-title {
                background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue));
                -webkit-background-clip: text;
                /* -webkit-text-fill-color: transparent; */ /* <--- REMOVE OR COMMENT THIS LINE */
                background-clip: text;
                font-size: 2.5rem;
                font-weight: 700;
                text-align: center;
                margin-bottom: 2rem;
                padding: 1rem 0;
            }

            /* Subtítulos elegantes */
            .section-header {
                color: var(--text-primary);
                font-size: 1.5rem;
                font-weight: 600;
                margin: 1.5rem 0 1rem 0;
                padding-bottom: 0.5rem;
                border-bottom: 2px solid var(--light-blue);
            }

            /* Tarjetas de información */
            .info-card {
                background: var(--card-bg);
                padding: 1.5rem;
                border-radius: 12px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                border: 1px solid var(--border-color);
                margin: 1rem 0;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }

            .info-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 25px -5px rgba(0, 0, 0, 0.15);
            }

            /* Sidebar mejorado */
            .css-1d391kg { /* Ajusta si el selector cambia con versiones de Streamlit */
                background: linear-gradient(180deg, var(--card-bg) 0%, #f9fafb 100%);
                border-right: 2px solid var(--border-color);
            }

            /* Pestañas modernas */
            .stTabs [data-baseweb="tab-list"] {
                background: var(--card-bg);
                border-radius: 12px;
                padding: 0.5rem;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                gap: 0.5rem;
            }

            .stTabs [data-baseweb="tab"] {
                background: transparent;
                border-radius: 8px;
                color: var(--text-secondary);
                font-weight: 500;
                padding: 0.75rem 1.5rem;
                transition: all 0.2s ease;
            }

            .stTabs [data-baseweb="tab"]:hover {
                background: var(--light-blue);
                color: var(--primary-blue);
            }

            .stTabs [aria-selected="true"] {
                background: var(--primary-blue) !important;
                color: white !important;
                font-weight: 600;
                box-shadow: 0 2px 8px rgba(37, 99, 235, 0.3);
            }

            /* Selectbox mejorado */
            .stSelectbox > div > div {
                background: var(--card-bg);
                border: 2px solid var(--border-color);
                border-radius: 8px;
                transition: border-color 0.2s ease;
            }

            .stSelectbox > div > div:focus-within {
                border-color: var(--primary-blue);
                box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
            }

            /* Alertas y mensajes mejorados */
            .stAlert {
                border-radius: 8px;
                border: none;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }

            /* Métricas visuales */
            .metric-card {
                background: var(--card-bg);
                padding: 1.5rem;
                border-radius: 12px;
                text-align: center;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                border-left: 4px solid var(--primary-blue);
            }

            .metric-value {
                font-size: 2rem;
                font-weight: 700;
                color: var(--primary-blue);
                margin-bottom: 0.5rem;
            }

            .metric-label {
                color: var(--text-secondary);
                font-weight: 500;
                text-transform: uppercase;
                font-size: 0.875rem;
                letter-spacing: 0.5px;
            }

            /* Responsive design */
            @media (max-width: 768px) {
                .main-title {
                    font-size: 2rem;
                }
                .section-header {
                    font-size: 1.25rem;
                }
            }

            /* Loading spinner personalizado */
            .stSpinner > div {
                border-top-color: var(--primary-blue) !important;
            }

            /* Botones mejorados */
            .stButton > button {
                background: var(--primary-blue);
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0.75rem 1.5rem;
                font-weight: 500;
                transition: all 0.2s ease;
            }

            .stButton > button:hover {
                background: var(--dark-blue);
                transform: translateY(-1px);
                box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);
            }

            /* Estilos para navegación personalizada (si decides usar botones en lugar de st.radio) */
            .nav-button {
                display: inline-block;
                padding: 0.5rem 1rem;
                margin: 0 0.25rem;
                background: var(--card-bg);
                border: 2px solid var(--border-color);
                border-radius: 8px;
                color: var(--text-primary);
                text-decoration: none;
                font-weight: 500;
                transition: all 0.2s ease;
            }
            .nav-button:hover {
                background: var(--primary-blue);
                color: white;
                border-color: var(--primary-blue);
            }
            .nav-button.active { /* Necesitarías lógica para añadir 'active' */
                background: var(--primary-blue);
                color: white;
                border-color: var(--primary-blue);
            }
        </style>
    """, unsafe_allow_html=True)