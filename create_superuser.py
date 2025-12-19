import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laptop_place_project.settings")
django.setup()

from django.contrib.auth.models import User

# --- CREDENTIALS ---
USERNAME = 'admin'  # Let's stick with 'admin' since it exists
PASSWORD = 'password123'  # Simple password for now
EMAIL = 'admin@example.com'

# Get the user (even if they already exist)
try:
    user = User.objects.get(username=USERNAME)
    print(f"User {USERNAME} found. Resetting password...")
except User.DoesNotExist:
    print(f"User {USERNAME} not found. Creating new...")
    user = User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)

# FORCE the password change
user.set_password(PASSWORD)
user.is_staff = True
user.is_superuser = True
user.save()

print(f"SUCCESS: Password for {USERNAME