from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
# Map /products to this -> index function
def index(request):
    products = Product.objects.all()
    # create an html template to present the list of products to the user
    return render(request, 'index.html', {'products': products})
    # {'products': products} is a dictionary

def new_products(request):
    return HttpResponse('New Products')

