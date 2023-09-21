from rest_framework import serializers
from item.models    import Item, Category, Car, CarType



class  ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model  = Item
    fields = ["id", 'category', "name", "description", "price", "image", "is_sold"]
    

class CarSerializer(serializers.ModelSerializer):


  class Meta:
    model  = Car
    fields = [ 'id', "Name", "Avilable_battries"]
