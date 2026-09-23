"""
fetch_data.py
Pulls top tracks, top artists, and recently played from the Spotify Web API
and stores snapshots for historical tracking.

Usage:
    python src/fetch_data.py
"""

import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from db import init_db, save_top_tracks, save_top_artists, save_recently_played

load_dotenv()

SCOPE = "user-top-read user-read-recently-played user-library-read"

def get_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=SCOPE
    ))

def fetch_top_tracks(sp, limit=20, time_range="medium_term"):
    results = sp.current_user_top_tracks(limit=limit, time_range=time_range)
    return results["items"]

def fetch_top_artists(sp, limit=20, time_range="medium_term"):
    results = sp.current_user_top_artists(limit=limit, time_range=time_range)
    return results["items"]

def fetch_recently_played(sp, limit=50):
    results = sp.current_user_recently_played(limit=limit)
    return results["items"]

if __name__ == "__main__":
    init_db()

    sp = get_spotify_client()
    top_tracks = fetch_top_tracks(sp)
    top_artists = fetch_top_artists(sp)
    recent = fetch_recently_played(sp)

    save_top_tracks(top_tracks)
    save_top_artists(top_artists)
    save_recently_played(recent)

    print(f"Saved {len(top_tracks)} top tracks to database")
    print(f"Saved {len(top_artists)} top artists to database")
    print(f"Saved {len(recent)} recently played items to database")
