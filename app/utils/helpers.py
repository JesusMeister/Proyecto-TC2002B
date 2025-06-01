# utils/helpers.py
import streamlit as st
import os

def create_platform_metrics(platform_folder):
    """Crear métricas básicas de la plataforma"""
    metrics = {}
    try:
        network_file = os.path.join(platform_folder, "network_plot.html")
        density_file = os.path.join(platform_folder, "density_plot.html")
        clusters_folder = os.path.join(platform_folder, "clusters")

        metrics['network_available'] = os.path.exists(network_file)
        metrics['density_available'] = os.path.exists(density_file)

        if os.path.exists(clusters_folder):
            cluster_files = [f for f in os.listdir(clusters_folder) 
                           if f.startswith("cluster_") and f.endswith(".html")]
            metrics['total_clusters'] = len(cluster_files)
        else:
            metrics['total_clusters'] = 0

    except Exception as e:
        # Considera retornar el error en lugar de mostrarlo directamente aquí,
        # para que la página que llama decida cómo manejarlo.
        # Por ahora, lo dejamos como st.error para mantener la funcionalidad original.
        st.error(f"Error al cargar métricas: {e}") 
        metrics['network_available'] = False
        metrics['density_available'] = False
        metrics['total_clusters'] = 0

    return metrics