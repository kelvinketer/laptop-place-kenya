from django.shortcuts import render
from .models import Product

def home(request):
    # 1. Get the search term from the URL (e.g., ?q=HP)
    query = request.GET.get('q')
    
    # 2. If a search term exists, filter the products
    if query:
        # 'icontains' means "Case-Insensitive Contains"
        # It finds "hp" inside "HP EliteBook" or "hP"
        products = Product.objects.filter(name__icontains=query)
    else:
        # 3. If no search, show all products
        products = Product.objects.all()

    return render(request, 'core/home.html', {
        'products': products,
        'query': query # Pass this back so we can keep it in the search bar
    })