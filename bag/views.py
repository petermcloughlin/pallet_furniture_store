from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_bag(request):
    ''' Displays the shopping bag contents page '''

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the particular product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    
    return redirect(redirect_url)


def amend_bag(request, item_id):
    """ Amend the quantity of the particular product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove an item from the shopping bag """

    try:
        quantity = int(request.POST.get('quantity'))

        bag = request.session.get('bag', {})

        if quantity > 0:
            del bag[item_id]
        else:
            bag.pop(item_id)    

        request.session['bag'] = bag
    
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)


