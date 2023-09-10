from django.db import models
# from item.models import Item
# Create your models here.


class CarType(models.Model):
  Name = models.CharField(max_length=2500)
  def __str__(self):
    return self.Name

class Car(models.Model):
  # car_type_choices= (
  #   ('BMW', 'BMW'),
  #   ('Lamborgene', 'Lamborgene')
  # )
  # Car_Type = models.CharField(max_length=255, choices=car_type_choices)
  
  Name = models.CharField(max_length=255);
  Car_type  = models.ForeignKey(CarType, on_delete=models.SET_NULL, default='', null=True, blank= True)
  Avilable_battries = models.ManyToManyField(to='item.Item', blank=True)

  
  def get_products(self):
      return ", ".join([p.name for p in self.Avilable_battries.all()])

  def get_products_object(self):

    if self.Avilable_battries.all():
      return  self.Avilable_battries.all()
    return False

  def __str__(self):
    return self.Name
  


