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
        'stripe_public_key': 'pk_test_51Qp6L7R0KkM8XZH6VLWDyO41n3tyel7XdyqigatIqFl67Q5BVdIXTYqENXDjkpq84eXlORDRsOTXqfWEPP2zVPTi006yWdKGgJ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)