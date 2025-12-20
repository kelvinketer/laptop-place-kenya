from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('student', 'Student'),
        ('business', 'Business'),
        ('gaming', 'Gaming'),
        ('accessories', 'Accessories'),
    ]

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    # New Field: Category
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='business')

    def __str__(self):
        return self.name
    