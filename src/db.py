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
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
