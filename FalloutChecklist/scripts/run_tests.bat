@echo off
REM Activate virtual environment if it exists
IF EXIST .venv\Scripts\activate.bat (
    CALL .venv\Scripts\activate.bat
)

cd ..
REM Run Django tests with verbosity=2
REM python manage.py test --verbosity=1
python manage.py test --verbosity=2
REM python manage.py test --verbosity=3
pause
