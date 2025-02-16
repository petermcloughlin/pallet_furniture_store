from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BespokeRequestForm


def bespokerequest_view(request):
    ''' View for Bespoke request form '''
    template = "bespokerequest/bespokerequest.html"
    form = BespokeRequestForm()
    
    if request.method == "POST":
        form = BespokeRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your request. \
                             A member of our team will be in contact \
                              with you within the next business day. ')
            return redirect("products")
        else:
            form = BespokeRequestForm()
            messages.error(request, 'Please ensure you add your name,\
                            contact number and email address.')

    context = {
        'form': form,     
    }
    return render(request, template, context)
