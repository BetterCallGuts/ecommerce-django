from django.shortcuts import render
from . import serializer
from django.http  import HttpRequest
from rest_framework.response import Response
from item.models import Item, Car
from rest_framework.decorators import api_view
from rest_framework            import status

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