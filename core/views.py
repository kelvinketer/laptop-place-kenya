from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator # Import the Paginator tool
from .models import Product

def home(request):
    # 1. Get query parameters
    query = request.GET.get('q')
    category_filter = request.GET.get('category')

    # 2. Filter products based on search or category
    if query:
        products_list = Product.objects.filter(name__icontains=query)
    elif category_filter:
        products_list = Product.objects.filter(category=category_filter)
    else:
        products_list = Product.objects.all().order_by('-id') # Show newest first

    # 3. SET UP PAGINATION (Show 8 laptops per page)
    paginator = Paginator(products_list, 8) 
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'core/home.html', {
        'products': products,
        'query': query
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # Get 3 related products
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[:3]
    return render(request, 'core/product_detail.html', {
        'product': product,
        'related_products': related_products
    })

def contact(request):
    return render(request, 'core/contact.html')