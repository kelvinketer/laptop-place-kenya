from django.contrib import admin
from django.urls import path
from core import views  # Import views from your core app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # New Path for Product Details
    # <int:pk> expects a number (ID) in the URL
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]