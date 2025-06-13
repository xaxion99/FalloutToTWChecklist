#!/bin/bash

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install -r requirements.txt
cd FalloutChecklist

# Start the Django server in the background
python manage.py runserver &

# Wait a bit for the server to start (adjust the sleep if needed)
sleep 2

# Open browser (use xdg-open for Linux, open for macOS)
if command -v xdg-open > /dev/null; then
  xdg-open http://127.0.0.1:8000/
elif command -v open > /dev/null; then
  open http://127.0.0.1:8000/
else
  echo "Open http://127.0.0.1:8000/ in your browser."
fi

# Bring the server process to the foreground (optional)
wait
