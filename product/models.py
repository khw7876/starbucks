from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256)
    

class Drink(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nutrition = models.TextField()
    allergy = models.TextField()
    
    
