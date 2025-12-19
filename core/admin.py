from django.contrib import admin
from .models import Product, Category

# This tells the admin panel to create a section for these two items
admin.site.register(Product)
admin.site.register(Category)