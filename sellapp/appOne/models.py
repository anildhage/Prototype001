from email.policy import default
from statistics import mode
from unicodedata import category
from django.db import models

# Create your models here.
class Seller(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)

class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100, null=True)

class Product(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100, null=True)
    price = models.IntegerField(default=0, null=True)
    desc = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True, upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True) 
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True) 





    
