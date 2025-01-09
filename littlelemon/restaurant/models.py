from django.db import models
from django.utils import timezone

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=100, default='Guest') 
    reservation_date = models.DateTimeField(default=timezone.now)
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name

class Menu(models.Model):
   name = models.CharField(max_length=100, default='Menu Item') 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'