from django.shortcuts           import render
from .                          import serializer
from django.http                import HttpRequest
from rest_framework.response    import Response
from item.models                import Item, Car
from rest_framework.decorators  import api_view
from rest_framework             import status
from django.contrib.auth.models import User
from django.contrib.auth        import authenticate 
from datetime                   import datetime
# Create your views here.


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
  
  all_cars  = Car.objects.all()
  all_items= Item.objects.all()


  itemserializer = serializer.ItemSerializer(all_items   ,many=True)
  carerializer   = serializer.CarSerializer (all_cars    ,many=True) 

  f = {
    "cars" : carerializer.data,
    "items" : itemserializer.data
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
  # print(req.data)
  
  
  username_ = req.data.get('username', None)
  password1 = req.data.get("password1", None)
  email    = req.data.get("email",    None)
  if (username_ and password1 and email) is not None:
    userrr = User.objects.filter(username=username_)
    userr = User.objects.filter(username=username_)
    if  userrr.exists() or userr.exists():
      
      
      return Response({"data" : None, "status" : "AlreadyExist"}, status=status.HTTP_200_OK)
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
