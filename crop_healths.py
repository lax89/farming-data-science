import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def plot_moisture_levels(crop_data):
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=crop_data['crop'],
        y=crop_data['moisture'],
        marker_color='#1565C0',
        name='Moisture Level'
    ))
    
    fig.update_layout(
        title='Crop Moisture Levels',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_color='#212121',
        yaxis_title='Moisture (%)'
    )
    
    st.plotly_chart(fig, use_container_width=True)

def display_crop_recommendations(crop_data):
    st.subheader("Crop Health Recommendations")
    
    for _, row in crop_data.iterrows():
        if row['health'] < 70:
            st.warning(f"{row['crop']}: Health is below optimal levels. Consider inspection and treatment.")
        if row['moisture'] < 40:
            st.warning(f"{row['crop']}: Low moisture detected. Consider irrigation.")
        elif row['moisture'] > 60:
            st.warning(f"{row['crop']}: High moisture detected. Monitor for disease risk.")
