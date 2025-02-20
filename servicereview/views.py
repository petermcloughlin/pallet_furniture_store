from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ServiceReviewForm


def review(request):
    ''' View for Service Review form '''
    template = "servicereview/servicereview.html"
    form = ServiceReviewForm()

    if request.method == "POST":
        form = ServiceReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your review. \
                             Your feedback is so important in  \
                             helping us improve our service. ')
            return redirect("products")
        else:
            form = ServiceReviewForm()
            messages.error(request, 'Please ensure you add your name,\
                            email address and a your review.')

    context = {
        'form': form,     
    }
    return render(request, template, context)