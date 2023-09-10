from django.shortcuts               import render, get_object_or_404
from item.models                    import Item
from django.contrib.auth.decorators import  login_required
from Car.models                     import  Car


@login_required
def index(request):
    items = Item.objects.filter(ordered_by=request.user)
    total = 0
    for n in items:
        total += n.price
        
    print(total)
    q = {
        'items' : items,
        'total' : total ,
        'forh' : Car.objects.all()
        }
    return render(request, 'dashboard/index.html', q)

