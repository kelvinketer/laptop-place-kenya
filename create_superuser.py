import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laptop_place_project.settings")
django.setup()

from django.contrib.auth.models import User

# --- CREDENTIALS ---
USERNAME = 'admin'
PASSWORD = 'password123'
EMAIL = 'admin@example.com'

# Get or Create User
try:
    user = User.objects.get(username=USERNAME)
    print(f"User {USERNAME} found.")
except User.DoesNotExist:
    print(f"Creating {USERNAME}...")
    user = User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)

# FORCE RESET PASSWORD
user.set_password(PASSWORD)
user.is_staff = True
user.is_superuser = True
user.save()

# This is the line that was broken before:
print(f"SUCCESS: Password for {USERNAME} set to {PASSWORD}")