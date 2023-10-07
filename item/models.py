from django.db import models
from django.contrib.auth.models import User
from Car.models                 import Car, CarType

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name 
    class Meta:
        ordering = ('name', )
        verbose_name_plural = "Categories"
    



class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True , null= True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    
    
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='items', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered_by = models.ManyToManyField(User, blank=True )
    
    
    def get_usrs_that_order_the_item(self):
        return [p for p in self.ordered_by.all()]
    
    
    def Supported_cars(self):
        Carss = Car.objects.filter(Avilable_battries__name =  self.name);
        Names = [x.Name for x in Carss]
        if len(Names) == 0:
            return "It doesn't support any Car"
        word = ''
        for i in Names:
            word += f'|{i}|'
        return f'{word}'
    
    def nameee(self):
        return str(self.name)
    
    
    def Supported_cars_template(self):
        Carss = Car.objects.filter(Avilable_battries__name =  self.name);
        Names = [x for x in Carss]
        if len(Names) == 0:
            return "It doesn't support any Car"
        word = []
        for i in Names:
            word.append(i)
        return word
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'products'



    # def how_to(self):
        
    #     return self.



# class Car(models.Model):
# 

class Ticket(models.Model):
    howMany = models.IntegerField();
    user    = models.ForeignKey(User, on_delete=models.CASCADE);
    item    = models.ForeignKey(Item, on_delete=models.CASCADE) 
    
    def __str__(self):
        
        return f"{self.user} | {self.item} | {self.howMany}"