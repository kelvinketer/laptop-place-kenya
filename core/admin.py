from django.contrib import admin
from .models import Product

# This class customizes how the list looks in the Admin Panel
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category') # Shows these columns
    list_filter = ('category',) # Adds a filter sidebar for categories
    search_fields = ('name',)   # Adds a search box

admin.site.register(Product, ProductAdmin)