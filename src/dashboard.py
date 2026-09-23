"""
dashboard.py
Streamlit dashboard for visualizing Spotify listening trends.

Usage:
    streamlit run src/dashboard.py
"""

import streamlit as st

st.set_page_config(page_title="My Spotify Analytics", layout="wide")
st.title("My Spotify Listening Analytics")
st.write("Dashboard coming soon — top artists, top tracks, and listening trends over time.")

# TODO: query SQLite data and render charts with st.bar_chart / st.line_chart
