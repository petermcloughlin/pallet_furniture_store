from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import StoreProduct

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0 
    delivery = 10
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(StoreProduct, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })
    if product_count > 0:
        grand_total = total + delivery
    else:
        grand_total = total    

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context