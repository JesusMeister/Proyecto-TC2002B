# components/ui_elements.py
import streamlit as st

def display_platform_overview(selected_platform, metrics):
    """Mostrar resumen de la plataforma seleccionada"""

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">📊</div>
                <div class="metric-label">Plataforma</div>
                <div style="font-weight: 600; color: var(--text-primary); margin-top: 0.5rem;">
                    {selected_platform.upper()}
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        status = "✅" if metrics.get('network_available', False) else "❌"
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{status}</div>
                <div class="metric-label">Red de Usuarios</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        status = "✅" if metrics.get('density_available', False) else "❌"
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{status}</div>
                <div class="metric-label">Análisis Densidad</div>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        cluster_count = metrics.get('total_clusters', 0)
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{cluster_count}</div>
                <div class="metric-label">Comunidades Encontradas</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

def app_footer():
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; color: var(--text-secondary); padding: 2rem 0;">
            <p>🔬 <strong>Dashboard de Análisis de Redes Sociales</strong></p>
            <p>Herramienta para visualización y análisis de patrones discursivos en redes sociales</p>
        </div>
    """, unsafe_allow_html=True)