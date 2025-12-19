import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'laptop_place_project.settings')
django.setup()

from django.contrib.auth.models import User

# Change these to whatever you want
USERNAME = 'admin2'
PASSWORD = 'password123'
EMAIL = 'info@laptopplacekenya.com'

if not User.objects.filter(username=USERNAME).exists():
    print(f'Creating superuser: {USERNAME}')
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
else:
    print('Superuser already exists.')