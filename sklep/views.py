from django.shortcuts import render
from .models import Product, Review, Order
from .forms import ProductForm


# Create your views here.
def products (request):
    products_list = Product.objects.all()
    return render(request, 'products.html', {'products_list':products_list})

def reviews (request):
    reviews_list = Review.objects.all()
    return render(request, 'reviews.html', {'reviews_list':reviews_list})



def add_product(request):
    if request.method == 'POST':
        productForm = ProductForm(request.POST)
        if productForm.is_valid():
            products_list = Product.objects.all()
            Product(name=request.POST["name"],description=request.POST["description"],price=request.POST["price"]).save()
            return render(request, 'products.html', {'products_list': products_list})
        else:
            return render(request, 'addproduct.html', {'form': productForm})
    else:
        productForm = ProductForm()
        return render(request, 'addproduct.html', {'form': productForm})

def orders (request):
    orders_list = Order.objects.all()
    return render(request, 'orders.html', {'orders_list':order_list})
