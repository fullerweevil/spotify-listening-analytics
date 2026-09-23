# Spotify Listening Analytics

A personal data project that tracks and visualizes my Spotify listening habits over time — top artists, top tracks, genre trends, and listening frequency — using the Spotify Web API, Python, and a Streamlit dashboard.

## Why This Project

I wanted a project that combined my interest in music/chart analytics with real backend and data engineering practice: OAuth authentication, API integration, persistent data storage, and data visualization.

## Tech Stack

- **Language:** Python
- **API:** Spotify Web API (via `spotipy`)
- **Storage:** SQLite
- **Dashboard:** Streamlit
- **Scheduling:** Local cron / scheduled script for periodic data pulls

## Features (Planned)

- [ ] Spotify OAuth (Authorization Code flow)
- [ ] Pull top tracks, top artists, and recently played
- [ ] Store snapshots in SQLite to build a listening history over time
- [ ] Dashboard: top artists/tracks, genre breakdown, listening trends by day/week
- [ ] Compare taste shifts over time (e.g., month over month)

## Setup

1. Clone the repo
2. Create a virtual environment: `python -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a Spotify app at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and set your Client ID/Secret as environment variables (see `.env.example`)
5. Run the data pull script: `python src/fetch_data.py`
6. Launch the dashboard: `streamlit run src/dashboard.py`

## Project Structure

```
spotify-listening-analytics/
├── src/
│   ├── fetch_data.py      # Pulls data from Spotify API
│   ├── db.py               # SQLite storage logic
│   └── dashboard.py        # Streamlit dashboard
├── data/                    # Local SQLite DB (gitignored)
├── requirements.txt
├── .env.example
└── README.md
```

## Status

🚧 Actively in development.
