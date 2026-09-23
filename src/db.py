"""
db.py
Handles SQLite storage for listening history snapshots.
"""

import sqlite3
from datetime import datetime

DB_PATH = "data/spotify_history.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS top_tracks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            track_name TEXT,
            artist_name TEXT,
            snapshot_date TEXT,
            time_range TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS top_artists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist_name TEXT,
            genres TEXT,
            snapshot_date TEXT,
            time_range TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS recently_played (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            track_name TEXT,
            artist_name TEXT,
            played_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_top_tracks(tracks, time_range="medium_term"):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    snapshot_date = datetime.now().strftime("%Y-%m-%d")
    for t in tracks:
        cur.execute(
            "INSERT INTO top_tracks (track_name, artist_name, snapshot_date, time_range) VALUES (?, ?, ?, ?)",
            (t["name"], t["artists"][0]["name"], snapshot_date, time_range)
        )
    conn.commit()
    conn.close()

def save_top_artists(artists, time_range="medium_term"):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    snapshot_date = datetime.now().strftime("%Y-%m-%d")
    for a in artists:
        genres = ", ".join(a.get("genres", []))
        cur.execute(
            "INSERT INTO top_artists (artist_name, genres, snapshot_date, time_range) VALUES (?, ?, ?, ?)",
            (a["name"], genres, snapshot_date, time_range)
        )
    conn.commit()
    conn.close()

def save_recently_played(items):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    for item in items:
        track = item["track"]
        cur.execute(
            "INSERT INTO recently_played (track_name, artist_name, played_at) VALUES (?, ?, ?)",
            (track["name"], track["artists"][0]["name"], item["played_at"])
        )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
