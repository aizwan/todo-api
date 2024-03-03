﻿## Installation Requirement
- make sure the computer/server already has the latest python version installed installed if not can get it from here https://www.python.org/downloads/windows/ for windows
- follow this guide for linux https://docs.python-guide.org/starting/install3/linux/

# Setup
- run command `python3 -m venv env` or `python -m venv env` for windows
- activate virtual environment with command `source env/bin/activate` or `env\Scripts\activate` for windows
- `pip install --upgrade pip`
- `pip install -r requirements.txt`

# Run once
`python manage.py migrate`

# To serve the api
`python manage.py runserver` but if running for local emulator use `python manage.py runserver 0.0.0.0:8000`
