import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laptop_place_project.settings")
django.setup()

from django.contrib.auth.models import User

# Check if admin exists, if not, create one
try:
    if not User.objects.filter(username='admin').exists():
        print("Creating default superuser...")
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superuser 'admin' created successfully!")
    else:
        print("Superuser 'admin' already exists.")
except Exception as e:
    print(f"Error creating superuser: {e}")