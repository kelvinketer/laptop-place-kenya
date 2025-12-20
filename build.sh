#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. Collect static files (The step that fixes the broken Admin styles)
python manage.py collectstatic --no-input

# 3. Migrate database (Ensures tables exist)
python manage.py migrate