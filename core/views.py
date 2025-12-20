from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    # Search logic
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'core/home.html', {
        'products': products,
        'query': query
    })

def product_detail(request, pk):
    # 'pk' stands for Primary Key (the ID number of the laptop)
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'core/product_detail.html', {'product': product})