from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    query = request.GET.get('q')
    category_filter = request.GET.get('category')

    if query:
        products = Product.objects.filter(name__icontains=query)
    elif category_filter:
        products = Product.objects.filter(category=category_filter)
    else:
        products = Product.objects.all()

    return render(request, 'core/home.html', {
        'products': products,
        'query': query
    })

def product_detail(request, pk):
    # 1. Get the current product
    product = get_object_or_404(Product, pk=pk)
    
    # 2. Get related products
    # Filter by same category, EXCLUDE the current one (pk=pk), and take the first 3
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[:3]

    return render(request, 'core/product_detail.html', {
        'product': product,
        'related_products': related_products
    })
    
    def contact(request):
    return render(request, 'core/contact.html')