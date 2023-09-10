from django.shortcuts               import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from item.models                    import Item
from .models                        import Conv
from .forms                         import ConvMessageForm
from Car.models                     import  Car




# @login_required
@login_required
def new_conv(request, item_pk):
    item = get_object_or_404(Item , pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    convs = Conv.objects.filter(item=item).filter(members__in=[request.user.id])
    
    if convs:
        return redirect('conv:detailconv', pk=convs.first().id)
    
    if request.method =='POST':
        form = ConvMessageForm(request.POST)
        if form.is_valid():
            conv = Conv.objects.create(item=item)
            conv.members.add(request.user)
            conv.members.add(item.created_by)
            conv.save()
            
            convmessage = form.save(commit=False)
            convmessage.conv = conv
            convmessage.created_by = request.user
            convmessage.save()
            return redirect('item:detail', pk=item_pk)
    else:
        form = ConvMessageForm
        
        x = {
            'form' : form,
            'forh' : Car.objects.all()
        }
        return render(request , 'conv/new.html', x)
    

@login_required
def inbox(request):
        convs = Conv.objects.filter(members__in=[request.user.id])
        inboxvars = {
            "convs" : convs,
            'forh' : Car.objects.all()
        }
        
        return render(request, 'conv/inbox.html', inboxvars)
    
    
@login_required
def detailconv(request, pk):
    convs = Conv.objects.filter(members__in=[request.user.id]).get(pk=pk)
    
    if request.method == "POST":
        form = ConvMessageForm(request.POST)
        
        if form.is_valid():
            convmessage = form.save(commit=False )
            convmessage.conv = convs
            convmessage.created_by = request.user
            convmessage.save()
            convs.save()
            
            return redirect('conv:detailconv' , pk=pk)
    else:
        form = ConvMessageForm()
    oldconvs = {
        'convs' : convs,
        'form' : form,
        'forh' : Car.objects.all()
    }
    return render(request, 'conv/detailconv.html', oldconvs)
