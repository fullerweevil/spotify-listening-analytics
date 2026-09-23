# Spotify Listening Analytics

A personal data project that tracks and visualizes my Spotify listening habits over time — top artists, top tracks, genre trends, and listening frequency — using the Spotify Web API, Python, and a Streamlit dashboard.

## Why This Project

I wanted a project that combined my interest in music/chart analytics with real backend and data engineering practice: OAuth authentication, API integration, persistent data storage, automation, and data visualization.

## Tech Stack

- **Language:** Python
- **API:** Spotify Web API (via `spotipy`)
- **Storage:** SQLite
- **Dashboard:** Streamlit
- **Scheduling:** macOS `cron` for automated daily data pulls

## Features

- [x] Spotify OAuth (Authorization Code flow)
- [x] Pull top tracks, top artists, and recently played
- [x] Store snapshots in SQLite to build a listening history over time
- [x] Dashboard: top artists/tracks, genre breakdown, listening trends by day/week
- [x] Automated daily data collection via cron
- [ ] Compare taste shifts over time (e.g., month over month)
- [ ] Deploy dashboard publicly (Streamlit Community Cloud)

## Setup

1. Clone the repo
2. Create a virtual environment: `python -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a Spotify app at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and set your Client ID/Secret as environment variables (see `.env.example`)
5. Run the data pull script: `python src/fetch_data.py`
6. Launch the dashboard: `streamlit run src/dashboard.py`

## Automation

Data is collected automatically once a day using a `cron` job, so the historical dataset builds up passively instead of relying on manual runs.

`run_fetch.sh` is a wrapper script that activates the virtual environment and runs `fetch_data.py`, logging output to `logs/fetch.log`.

To set this up on your own machine:

1. Edit `run_fetch.sh` and update the `cd` path to match your local clone location.
2. Make it executable: `chmod +x run_fetch.sh`
3. Add a cron entry: `crontab -e`, then add a line like:
   ```
   0 9 * * * /absolute/path/to/spotify-listening-analytics/run_fetch.sh
   ```
4. Check `logs/fetch.log` to confirm scheduled runs are succeeding.

## Project Structure

```
spotify-listening-analytics/
├── src/
│   ├── fetch_data.py      # Pulls data from Spotify API
│   ├── db.py               # SQLite storage logic
│   └── dashboard.py        # Streamlit dashboard
├── data/                    # Local SQLite DB (gitignored)
├── logs/                    # Cron job logs (gitignored)
├── run_fetch.sh             # Cron wrapper script
├── requirements.txt
├── .env.example
└── README.md
```

## Status

🚀 Core pipeline complete: OAuth, data collection, storage, automation, and dashboard are all working. Actively adding deeper trend analysis.
