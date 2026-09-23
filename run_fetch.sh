#!/bin/bash
cd /Users/fullerweevil/Desktop/General/VS_projects/spotify-listening-analytics
source venv/bin/activate
python3 src/fetch_data.py >> logs/fetch.log 2>&1
