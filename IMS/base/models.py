from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=False)
    quantity = models.IntegerField()
    price = models.IntegerField()

    STATUS_CHOICES = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item sold'),
        ('RESTOCKING', 'Item restocking in few days'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='SOLD') # Available, Sold, Restocking
    issues = models.CharField(max_length=10, default="No issues") 

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type : {0} Quantity : {1} Price : {2}'.format(self.type, 
                    self.quantity, self.price)
    
    
class Laptop(Product):
    pass

class Desktop(Product):
    pass

class Mobile(Product):
    pass    
