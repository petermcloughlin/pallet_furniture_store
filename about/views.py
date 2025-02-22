from django.shortcuts import render


def about(request):
    ''' Display the about page '''
    template = 'about/about.html'

    return render(request, template)
