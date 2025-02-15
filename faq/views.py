from django.shortcuts import render
from .models import Faq
# Create your views here.


def faq(request):
    ''' display the FAQ page '''
    template = 'faq/faq.html'

    context = {
        'faqs': Faq.objects.all(),
    }

    return render(request, template, context)
