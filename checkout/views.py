from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import CustomerOrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your shopping bag.')
        return redirect(reverse('products'))
    
    order_form = CustomerOrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)