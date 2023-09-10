from django.shortcuts       import render, redirect
from item.models            import  Category, Item
from django.contrib.auth    import logout
from django.contrib         import messages
from Car.models             import Car
from .forms                 import SignupForm
from django.http            import HttpRequest











def landing(req:HttpRequest):
    all_category = Category.objects.all()
    
    var = {
        'categorys' : all_category,
        'forh' : Car.objects.all()
    }
    
    return render(req, 'core/landing.html', var)









def index(request):
    items    = Item.objects.filter(is_sold=False)
    category = Category.objects.all()
    listt    = {
        'category' : category,
        "items" :     items,
        'forh' : Car.objects.all()
        
    }
    
    return render(request, 'core/index.html', listt)


def contact(request):
    x = {'forh' : Car.objects.all()}
    return render(request, "core/contact.html",x)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():

            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    a = {
        'form' : form,
        'forh' : Car.objects.all()
    }
    return render(request, 'core/signup.html',a)


def logout_user(request ):
    logout(request)
    messages.success(request, ("Loggedout succefully !"))
    return redirect('core:landing')