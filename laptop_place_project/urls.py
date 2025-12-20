from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('contact/', views.contact, name='contact'),

    # Temporary link to create admin
    path('create-admin-user/', views.create_superuser),
]