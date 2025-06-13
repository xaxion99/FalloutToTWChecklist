@echo off
if not exist .venv (
    python -m venv .venv
)
call .venv\Scripts\activate
pip install -r requirements.txt
cd FalloutChecklist

REM Start Django server in a new window and open browser
start "" python manage.py runserver
start http://127.0.0.1:8000/
pause
