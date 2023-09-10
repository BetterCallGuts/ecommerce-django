from django.shortcuts import (
                            render,
                            get_object_or_404,
                            redirect,
                            )
from .models import Item, Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm
from Car.models import Car, CarType
# Create your views here.


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


def items(request, pk=None):

    # for i in items:
    #     if i in selected_object:
    #         continue
    #     selected_object.append(i)
    tolow   = False
    tohigh  = False
    
    ispricetohigh = False
    ispricetolow  = False
    
    check = []
    query = request.GET.get('query', False)
    datasortby = request.GET.get('sorted', 0)
    category_id = request.GET.get('category',0)
    # pricesort   = request.GET.get('isprice', 0)
    # car_id      = request.GET.get('car',0)
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
        # print(ite)
        # items = items.filter(name=the_bettery_form_car.Avilable_battries)
    selected_object = []
    for i in Car.objects.all():
        itemname = request.GET.get(str(i.Name), False)
        # print(itemname)
        # print(query)
        # print(type(query))
        # print(str(query))
        # if  i.Name.lower().strip().find(str(query)) != -1:
        #     # print(str(query).lower() in str(i.Name))
        #     print(query, "**", i.Name)
        #     if i.get_products_object():
        #         for s in i.get_products_object():
        #             # print('*', s)
        #             # print(s, end='', flush=1)
        #             if s in selected_object:
        #                 continue
        #             selected_object.append(s)
            
        if itemname:
            check.append(i) 
            if i.get_products_object():
                for s in i.get_products_object():
                    # print('*', s)
                    # print(s, end='', flush=1)
                    if s in selected_object:
                        continue
                    selected_object.append(s)
            else:
                selected_object.append(i.get_products_object(   ))
    # print(selected_object)
    selected_object_wanted = []
    wanted_items           = []
    wanted_filter = Car.objects.filter(Q(Name__icontains=str(query).lower()))
    # print(wanted_filter)
    for s in wanted_filter:
        # print(s)
        selected_object_wanted.append(s.get_products_object())
    
    for m in selected_object_wanted:
        # print(m)
        if  m:
            for n in m:
                if n in wanted_items:
                    continue
                # print('Got Access')
                wanted_items.append(n)
                
    # print(wanted_items)

    
    # print(selected_object)    


    if selected_object and wanted_items:
            # print(selected_object_wanted)
            # print('got access')
            selected_object = list(set(selected_object).intersection(wanted_items))

        
    else:
        selected_object = selected_object_wanted
        
    # print(selected_object)
        
        
        
    # print(selected_object)
    # for i in selected_object:
    #     for s in i:
    #         print(s, end="", flush=True)
    #     print(' ')
        # selected_object.append(itemname)
        
        # print(itemname)
        # print(i.Name)
        

    # print(selected_object)
    # print(request.GET)
    # the_bettery_form_car = Car.objects.get(id=car_id)
    # items = the_bettery_form_car.get_products_object()
    # print(check)
        
    finished = []
    if category_id:
        items = items.filter(category_id=category_id)
    
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    # print( items )
    s = []
    # if selected_object :
    for i in selected_object:
        # print(i)
        # print(i)
        # if type(i) == bool:
        #     continue
        if is_iterable(i):
            for l in i:
                # print(l)

                if l in s:
                    continue
                s.append(l)
        else:
            if i in  s:
                continue
            s.append(i)

    # print(s)
    selected_object = s
    if datasortby:
        # print(datasortby)
        if datasortby == "isuppertime":
            items = items.order_by('created_at')
            datasortby = 1
        
        elif datasortby == "islowertime":
            items = items.order_by('-created_at')
            datasortby = 2
        
        elif datasortby == "isupperprice":
            items = items.order_by('price')
            datasortby = 3
        
        elif datasortby == "islowerprice":
            items = items.order_by('-price')  
            datasortby = 4  
    # print(selected_object)
    # print(items)
    # print('*'*10)
    # print(selected_object)
    # print(items)
    if len(selected_object) >= 1:
        # print(False)
        if len(items) > 0:
        # for i in selected_object:
        #     if items.filter(pk=i.pk).exists():
        #         finished.append(i)
            for l in items:
                for s in selected_object:
                    if l == s:
                        finished.append(l)
        else:
        
            finished = selected_object
            # print("got access")
            # print(finished)

    else:
        # print(True)
        finished = items
    # print(items)

    # for i in items:
    #     if i in selected_object:
    #         continue
    #     selected_object.append(i)
    
    all_cars = Car.objects.all()
    o = []
    # for i in finished:

    # finished = list(set(finished))
    # print(finished)
    print(finished)
    if len(wanted_filter) > 0 :
        for i in finished:
            print('passforloop')
            # print("AAAAA")
            print(i)
            if is_iterable(i):
                print("good iterable")
                for l in i:
                    # print(l)

                    if l in o:
                        
                        print("it was in ")
                        continue
                    print("It got appedned")
                    o.append(l)
            else:
                if i in o:
                    continue
                o.append(i)
        finished = o
    # print('*'*10)
    # print(o)
    # for i in o:
    #     print(i.pk)
    #     print(i.name)

    if not query:
        query = ''
        
    print(finished)
        
    return render(request, 'item/items.html', {
        'items'  : finished,
        'query'  : query,
        'categories' : categories,
        'category_id' : int(category_id),
        'all_cars' : all_cars,
        'checks' : check,
        'selected'   : datasortby,
        'forh' : Car.objects.all(),
        # 'car_id'    :int(car_id),
    })

def  detail(request, pk):
    button = False
    item = get_object_or_404(Item , pk=pk)
    m    = request.GET.get('m', None)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)
    # print(item.Supported_cars())
    
    if request.method == 'POST':
        m = 'was removed successfuly!';
        l = Item.objects.get(pk=pk);
        l.ordered_by.remove(request.user);
    
    try:
        g = item.ordered_by.get(id=request.user.id)
        button = True
    except:
        pass
    d = {
        'button': button,
        'item' : item,
        'related_items' : related_items,
        'm':m,
        'forh' : Car.objects.all()
        
    }
    
    return render(request, 'item/detail.html', d)

@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    
    c= {
        'form' : form,
        'title' : 'New item',
        'forh' : Car.objects.all()
    }
    return render(request, 'item/form.html' ,c)

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == "POST":
        form = EditI
        temForm(request.POST, request.FILES, instance=item)
        
        if form.is_valid():
            
            form.save()
            
            
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)
    
    c= {
        'form' : form,
        'title' : 'Edit item',
        'forh' : Car.objects.all()
    }
    return render(request, 'item/form.html' ,c)



@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    
    return redirect('dashboard:index')