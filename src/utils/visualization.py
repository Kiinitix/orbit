import plotly.graph_objects as go
import streamlit as st

def visualize_graph(graph_data):
    st.title("Project Dependency Manager")

    fig = go.Figure()
    for edge in graph_data["edges"]:
        fig.add_trace(go.Scatter(
            x=[edge["source"]["x"], edge["target"]["x"]],
            y=[edge["source"]["y"], edge["target"]["y"]],
            mode='lines',
            line=dict(width=1, color='blue'),
            hoverinfo='none'
        ))
    for node in graph_data["nodes"]:
        fig.add_trace(go.Scatter(
            x=[node["x"]],
            y=[node["y"]],
            mode='markers+text',
            text=node["name"],
            textposition="bottom center",
            marker=dict(size=10, color='red'),
            hoverinfo='text'
        ))
    st.plotly_chart(fig)
