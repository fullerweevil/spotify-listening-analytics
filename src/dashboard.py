"""
dashboard.py
Streamlit dashboard for visualizing Spotify listening trends.

Usage:
    streamlit run src/dashboard.py
"""

import sqlite3
import pandas as pd
import streamlit as st
from collections import Counter

DB_PATH = "data/spotify_history.db"

st.set_page_config(page_title="My Spotify Analytics", layout="wide")
st.title("My Spotify Listening Analytics")
st.caption("Personal listening trends pulled from the Spotify Web API and tracked over time.")

@st.cache_data(ttl=60)
def load_data():
    conn = sqlite3.connect(DB_PATH)
    top_tracks = pd.read_sql_query("SELECT * FROM top_tracks", conn)
    top_artists = pd.read_sql_query("SELECT * FROM top_artists", conn)
    recently_played = pd.read_sql_query("SELECT * FROM recently_played", conn)
    conn.close()
    return top_tracks, top_artists, recently_played

top_tracks, top_artists, recently_played = load_data()

if top_tracks.empty and top_artists.empty:
    st.warning("No data yet. Run `python src/fetch_data.py` first to pull your Spotify data.")
    st.stop()

snapshot_dates = sorted(top_tracks["snapshot_date"].unique(), reverse=True)
latest_snapshot = snapshot_dates[0]

st.sidebar.header("Filters")
selected_snapshot = st.sidebar.selectbox("Snapshot date", snapshot_dates, index=0)

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"Top Artists ({selected_snapshot})")
    artists_snapshot = top_artists[top_artists["snapshot_date"] == selected_snapshot]
    artist_counts = artists_snapshot["artist_name"].value_counts().head(10)
    st.bar_chart(artist_counts)

with col2:
    st.subheader(f"Top Tracks ({selected_snapshot})")
    tracks_snapshot = top_tracks[top_tracks["snapshot_date"] == selected_snapshot]
    st.dataframe(
        tracks_snapshot[["track_name", "artist_name"]].reset_index(drop=True),
        use_container_width=True,
        hide_index=True
    )

st.subheader("Genre Breakdown")
genre_list = []
for genres in artists_snapshot["genres"].dropna():
    genre_list.extend([g.strip() for g in genres.split(",") if g.strip()])

if genre_list:
    genre_counts = pd.Series(Counter(genre_list)).sort_values(ascending=False).head(15)
    st.bar_chart(genre_counts)
else:
    st.info("No genre data available for this snapshot.")

st.subheader("Recently Played (Most Recent 20)")
if not recently_played.empty:
    recent_display = recently_played.sort_values("played_at", ascending=False).head(20)
    st.dataframe(
        recent_display[["track_name", "artist_name", "played_at"]].reset_index(drop=True),
        use_container_width=True,
        hide_index=True
    )

if len(snapshot_dates) > 1:
    st.subheader("Top Artist Appearances Across Snapshots")
    pivot = (
        top_artists.groupby(["snapshot_date", "artist_name"])
        .size()
        .reset_index(name="count")
        .pivot(index="snapshot_date", columns="artist_name", values="count")
        .fillna(0)
    )
    top_recurring = top_artists["artist_name"].value_counts().head(8).index
    st.line_chart(pivot[[c for c in top_recurring if c in pivot.columns]])
else:
    st.info("Run fetch_data.py again on a different day to unlock trend-over-time charts.")
