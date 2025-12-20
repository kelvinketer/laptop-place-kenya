#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. CLEAR and Collect static files (Fixes the 0 files copied error)
python manage.py collectstatic --no-input --clear

# 3. Migrate database
python manage.py migrate