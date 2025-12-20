from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    query = request.GET.get('q')
    category_filter = request.GET.get('category')  # Check if a category button was clicked

    if query:
        # Search functionality
        products = Product.objects.filter(name__icontains=query)
    elif category_filter:
        # Category functionality (e.g. ?category=gaming)
        products = Product.objects.filter(category=category_filter)
    else:
        # Show everything
        products = Product.objects.all()

    return render(request, 'core/home.html', {
        'products': products,
        'query': query
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'core/product_detail.html', {'product': product})