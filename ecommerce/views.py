from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''
    
    return HttpResponse('Welcome to 6410742032 Sittipak Srisawas views!')

def item_view(request, item_id):   
    
    context_data = {
        "item_id": item_id   
    }

    return render(request, 'index.html',context= context_data)

def homepage_view(request):   
    
    return render(request, 'homepage.html')

def catagory_view(request):   
    
    return render(request, 'catagory.html')

def product_view(request):   
    
    return render(request, 'product.html')

def checkout_view(request):   
    
    return render(request, 'checkout.html')

def contact_view(request):   
    
    return render(request, 'contact.html')
