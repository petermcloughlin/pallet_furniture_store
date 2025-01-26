from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import StoreProduct

# Create your views here.

def all_products(request):
    ''' A view to display all products '''

    products = StoreProduct.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'You must enter a search criteria.')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, storeproduct_id):
    ''' A view to display a single products details '''

    product = get_object_or_404(StoreProduct, pk=storeproduct_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)