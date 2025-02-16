from django.shortcuts import render

# Create your views here.
def about(request):
    ''' Display the about page '''
    template = 'about/about.html'

    return render(request, template)
