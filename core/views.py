from django.shortcuts import render
from .models import Product, Category

def home(request):
    # 1. Get all products from the database
    products = Product.objects.all()
    
    # 2. Get categories (for that row of icons)
    categories = Category.objects.all()
    
    # 3. Send them to the HTML template
    return render(request, 'core/home.html', {
        'products': products,
        'categories': categories,
    })
    
    from django.shortcuts import render, get_object_or_404 # <--- ADD get_object_or_404 HERE
from .models import Product, Category

def home(request):
    # ... (Keep your existing home code here) ...
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/home.html', {
        'products': products,
        'categories': categories,
    })

# --- ADD THIS NEW FUNCTION BELOW ---
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'core/product_detail.html', {'product': product})