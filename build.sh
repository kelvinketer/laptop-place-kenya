#!/usr/bin/env bash
# Exit on error
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. Collect static files (The --clear flag fixes the "0 files" bug)
python manage.py collectstatic --no-input --clear

# 3. Migrate database
python manage.py migrate