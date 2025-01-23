from django.shortcuts import render, get_object_or_404
from .models import StoreProduct

# Create your views here.

def all_products(request):
    ''' A view to display all products '''

    products = StoreProduct.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, storeproduct_id):
    ''' A view to display a single products details '''

    product = get_object_or_404(StoreProduct, pk=storeproduct_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)