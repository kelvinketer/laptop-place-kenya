from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100) # e.g. "Business", "Student", "Gaming"
    image = models.ImageField(upload_to='categories/', blank=True, null=True) # For those green circular icons

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    # Basic Info
    name = models.CharField(max_length=255) # e.g. "HP EliteBook 840 G3"
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    brand = models.CharField(max_length=50, default="HP") # e.g. HP, Dell, Lenovo (for the sidebar filter)
    price = models.IntegerField() # e.g. 79500
    old_price = models.IntegerField(null=True, blank=True) # To show the strikethrough price if on sale
    
    # Specs (seen on your product page)
    processor = models.CharField(max_length=100) # e.g. "Intel Core i5 6th Gen"
    ram = models.CharField(max_length=50) # e.g. "8GB DDR4"
    storage = models.CharField(max_length=50) # e.g. "256GB SSD"
    display = models.CharField(max_length=50) # e.g. "14 inch FHD"
    
    # Marketing
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/') # The main laptop photo
    is_featured = models.BooleanField(default=False) # Check this to make it appear on the Homepage "Trending Deals"
    green_friday_deal = models.BooleanField(default=False) # Check this to show the "Green Friday Bonus" box

    def __str__(self):
        return self.name