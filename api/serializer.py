from rest_framework import serializers
from item.models    import Item, Category, Car, CarType
from django.contrib.auth  import models


class  ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model  = Item
    fields = ["id", 'category', "name", "description", "price", "image", "is_sold", "ordered_by"]
    

class CarSerializer(serializers.ModelSerializer):


  class Meta:
    model  = Car
    fields = [ 'id', "Name", "Avilable_battries"]



class UserSerializer(serializers.ModelSerializer) : 
  class Meta:
    model  = models.User
    fields = "__all__"
    


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model  = Category
    fields = ['id', 'name']