# Fallout Tale of Two Wastelands Checklist

This repository contains a Django application for tracking collection and achievement progress in the Fallout games. The project can be run locally using either the provided shell script or Windows batch file.

## Setup

1. Create a virtual environment in the repository root and install the required packages:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
   On Windows, use:
   ```bat
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Start the development server:
   - **Linux/macOS**: run `./start_checklist.sh`
   - **Windows**: run `start_checklist.bat`

Both scripts will activate the virtual environment, install dependencies, and launch the Django server at `http://127.0.0.1:8000/`.

## Running Tests

From within the `FalloutChecklist` directory, run:
```bash
scripts/run_tests.sh
```
Alternatively, call the script with its full path: `bash FalloutChecklist/scripts/run_tests.sh`.
