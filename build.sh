#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "1. Installing requirements..."
pip install -r requirements.txt

echo "2. Collecting static files..."
python manage.py collectstatic --no-input --clear

echo "3. Migrating database..."
python manage.py migrate

echo "4. Checking for Superuser..."
python create_superuser.py