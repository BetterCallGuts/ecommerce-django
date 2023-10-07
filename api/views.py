from django.shortcuts           import render
from .                          import serializer
from django.http                import HttpRequest
from rest_framework.response    import Response
from item.models                import Item, Car, Category, Ticket
from rest_framework.decorators  import api_view
from rest_framework             import status
from django.contrib.auth.models import User
from django.contrib.auth        import authenticate 
from datetime                   import datetime
import time
import stripe
# Create your views here.



stripe.api_key = 'sk_test_51NnyOqLRRSW6cJT8FxnIm7hY9ZYZQNAq1ePn7zCVZtCOiSRwppcw7VC0uu893Ozy8tWjZNRTjA3JYyi2tfzhwnnd00ZSXeTMeX'


@api_view(['GET'])
def getallitems(req:HttpRequest, format=None):
  allitem = Item.objects.all()
  itemserialzed  = serializer.ItemSerializer(allitem, many=True)
  
  
  
  return Response(itemserialzed.data, status=status.HTTP_200_OK )


@api_view(['GET'])
def getallcarstype(req, format=None):
  
  allcars = Car.objects.all()
  carserialzed = serializer.CarSerializer(allcars, many=True)

  
  carserialzed.data[0]["Name"]

        
  
  
  return Response(carserialzed.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def getalldata(req, format=None):
  
  all_cars       = Car.objects.all()
  all_items      = Item.objects.all()
  all_categories = Category.objects.all()

  itemserializer       = serializer.ItemSerializer(all_items   ,many=True)
  carerializer         = serializer.CarSerializer (all_cars    ,many=True) 
  categoriesserializer = serializer.CategorySerializer(all_categories, many=True)


  f = {
    "cars" : carerializer.data,
    "items" : itemserializer.data,
    'categories' : categoriesserializer.data
    }
  
  
  return Response(f, status=status.HTTP_200_OK)



@api_view(["POST"])
def check_user(req:HttpRequest, format= None):
  
  
  print(req.data)
  username = req.data.get('username', '')
  password = req.data.get('password', '')
  print(username, "  " , password)
  try:
    the_user = authenticate(req, username=username, password=password)
    if the_user is None:
      print("The user is none lamo")
      the_res_data = {
      "status"   : status.HTTP_404_NOT_FOUND,
      "the_user" : None
                        } 
      return Response(the_res_data, status=status.HTTP_404_NOT_FOUND)
    name = the_user.get_username()
    the_user = User.objects.get(username=name)

  
  except User.DoesNotExist:
    the_user = None
  
  
  if the_user is None:
    the_res_data = {
      "status"   : status.HTTP_404_NOT_FOUND,
      "the_user" : None
    } 
    
    return Response(the_res_data, status=status.HTTP_404_NOT_FOUND)

    
    
  userserialized = serializer.UserSerializer(the_user)
  
  return Response(userserialized.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createuser(req:HttpRequest, format=None):
  print(req.data)
  print("*"*10)
  print(req.POST)
  
  
  username_ = req.data.get('username', None)
  password1 = req.data.get("password1", None)
  email    = req.data.get("email",    None)
  if (username_ and password1 and email) is not None:
    userrr = User.objects.filter(username=username_)
    userr = User.objects.filter(email=email)
    if  userrr.exists() :
      
      
      return Response({"data" : None, "status" : "Username Already exists"}, status=status.HTTP_409_CONFLICT )
    elif userr.exists():
      
      return Response({"data" : None, "status" : "Email Already exists"}, status=status.HTTP_409_CONFLICT )
    else:
  

      newuser = User.objects.create( username=username_,email=email, password=password1)
      statust  = "success"
      f = {
        "data" : {
          "id" : newuser.pk,
          "username": newuser.username,
          "email"   : newuser.email
          },
        "status": statust
      }
      return Response(f, status=status.HTTP_201_CREATED)




@api_view(['GET', "POST"])
def getcart(req:HttpRequest, format=None):
  

  user              = req.data.get('userid', 0);
  try:
    user              = User.objects.get(pk=user);
  except User.DoesNotExist:
    pass
  tickets           = Ticket.objects.filter(user=user); 
  ticketsserialier  = serializer.TicketSerialier(tickets, many=True) 
  
  return Response(ticketsserialier.data, status=status.HTTP_200_OK);

@api_view(['GET', "POST"])
def getitemcartforuser(req, format=None):
  
  print(req)
  print(req.data)
  user = req.data.get('userid', 0)
  item = req.data.get("itemid", 0)


  try:
    item   = Item.objects.get(pk=item)
    user   = User.objects.get(pk=user)
    ticket = Ticket.objects.get(user=user, item=item) 

  
  except Ticket.DoesNotExist:
    
    print('*'*50)
    
    data = {
    "status" : 200,
    "howmany": 0  ,
    "masseg" : "Success"
  }
    return Response(data, status=status.HTTP_200_OK)

  except:
    pass

  howmany = ticket.howMany
  
  data = {
    "status" : 200,
    "howmany": howmany,
    "masseg" : "Success"
  }
  return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def addtocart(req:HttpRequest , format=None):
  user    = req.data['userid']         ;
  item    = req.data['itemid']         ;
  howmany = req.data['howmany']        ;
  item    = Item.objects.get(pk=item)  ;
  user    = User.objects.get(pk=int(user))  ;
  objecE  = Ticket.objects.filter(user=user, item=item)
  
  if objecE.exists():
    thedata = objecE.first()
    thedata.howMany += howmany

    print(thedata.howMany)
    thedata.save()

  else:
      
    new_ticket = Ticket.objects.create(howMany=howmany, user=user, item=item)
    print(new_ticket)
    
    new_ticket.save()
  
  res = {
    "status" : "success",
    "massege": "The ticket added succefully"
  }
  
  return Response(res, status=status.HTTP_201_CREATED)



@api_view(['GET', 'POST'])
def getallcartforuser(req:HttpRequest, format=None):

  try:
    user    = req.data.get('userid', None);
    user    = User.objects.get(pk=user) 
    ticktes = Ticket.objects.filter(user=user) 
    if ticktes.exists():
      items = []
      for ticket in ticktes:
        item = ticket.item
        items.append(item)
        # print(item)
      itemserialized = serializer.ItemSerializer(items, many=True)

        
      data = {
          "status" :  "200",
          "masseg" : "Success",
          "data"   : itemserialized.data,
          "empty"  : False  
        }
      return Response(data, status=status.HTTP_200_OK)
    
  except User.DoesNotExist:
    pass
  
  
  data = {
    "status" :  "200",
    "masseg" : "Success",
    "data"   : None,
    "empty"  : True
  }
  
  return Response(data, status=status.HTTP_200_OK)


@api_view(['POST' ])
def hepaid(req):
  
  user    = req.data.get('userid', None)
  user    = User.objects.get(pk=user)
  tickets = Ticket.objects.filter(user=user) 
  for ticket in tickets:
    ticket.delete()


  data = {
    "status" : 200,
    "masseg" : "Success",
    "data"   : None
  }
  return Response(data, status=status.HTTP_200_OK)
  
  
  
  
  

@api_view(['POST', "GET"])
def update_cart(req:HttpRequest):
  try:
    userid = req.data.get('userid' , None)
    print('userid', userid)
    itemid = req.data.get('itemid' , None)
    print('itemid', itemid)
    howmuch= req.data.get('howmuch', None)
    print('howmuch', howmuch)
    user   = User.objects.get(   pk=int(userid))
    print('got user ' , user)
    item   = Item.objects.get(  pk=itemid)
    ticket = Ticket.objects.get(user=user, item=item)
    ticket.howMany = int(howmuch)
    ticket.save()
    data = {
      "howmany" : int(ticket.howMany),
      "masseg"  : "Updated Succefully!",
      "status"  : 200
    }
  except User.DoesNotExist():
    print('userProblem')
  except Ticket.DoesNotExist():
    ...
    print('ticketproblem')
  except Item.DoesNotExist():
    print("Item problem")
  except :
    ...
    print('idk probplem')
  
  
  print("*"*10)
  print(req.data)
  
  
  
  return Response(data, status=status.HTTP_200_OK)



@api_view([ ])
def payment_api_for_one_item(req):
  
  

  amount         = req.data.get('amount', None)
  username       = req.data.get('username', None)
  token          = req.data.get('stripeToken', None)
  ticketfinished = req.data.get('ticket', None) 
  # print('*'*10)   
  # print(type(token))
  # print(email)
  # print('*'*10)   
  # print(req.user.email)
  
  
  total = 0
  
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
    description='pay for the cart one item'
    
    

  )
  
      
      
  data = {}
  return Response(data,status=status.HTTP_202_ACCEPTED)



@api_view(['POST', "GET"])
def deleteoneitemfromcart(req:HttpRequest):
  userid = req.data.get('userid', None)
  itemid = req.data.get('itemid', None)
  user   = User.objects.get(pk=userid)
  item   = Item.objects.get(pk=itemid)
  ticket = Ticket.objects.get(user=user, item=item)
  ticket.delete()

  
  
  
  return Response(
    {
    },
    status=status.HTTP_200_OK
)
  