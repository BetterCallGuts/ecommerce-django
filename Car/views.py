
from django.shortcuts import render, redirect
from item.models      import Item
from django.http      import HttpRequest
# Create your views here.
from item.views       import detail
from django.contrib.auth.decorators  import  login_required
import stripe
from django.urls  import reverse
from .models      import Car

stripe.api_key = 'sk_test_51NnyOqLRRSW6cJT8FxnIm7hY9ZYZQNAq1ePn7zCVZtCOiSRwppcw7VC0uu893Ozy8tWjZNRTjA3JYyi2tfzhwnnd00ZSXeTMeX'

@login_required()
def add_cart(req:HttpRequest, pk):
  
  the_item = Item.objects.get(pk = pk)
  
  the_item.ordered_by.add(req.user)


  # print(str(reverse('item:detail')) + f"{pk}?m=Add")
  
  # print(reverse('item:detail'))
  # return redirect(f'http://192.168.1.11:4040/item/{pk}?m=Is Added succefully !')
  # return redirect(str(reverse('item:detail', args=(pk,  ))) + "?m=Add")
  return redirect(f'http://192.168.1.113:2020/item/{pk}?m=Added successfuly!')
# 
@login_required
def payment(req):

    
  
  x = {
    'forh' : Car.objects.all()
  }  
  return render(req, "Car/payment.html",x)



def paymentaccepted(req:HttpRequest):

  # print(req.POST)
  if req.method == 'POST':
    email    = req.POST['email']
    username = req.POST['username']
    token    = req.POST.get('stripeToken', None)
    print('*'*10)   
    print(type(token))
    # print(email)
    print('*'*10)   
    # print(req.user.email)
    if email == str(req.user.email):
      
      items = Item.objects.filter(ordered_by=req.user)
      total = 0
      for n in items:
        total += n.price
      # print(req.POST)
      customer = stripe.Customer.create(
        email = email,
        name  = username,
        source= token
      )
      charge = stripe.Charge.create(
        customer=customer,
        amount= int(total *100),
        currency='usd',
        description='pay for the cart'
        
        

      )
      
      
      for n in items:
        n.ordered_by.remove(req.user)


    
  
  
  
  return redirect(reverse('core:index'))