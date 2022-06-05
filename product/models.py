from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name



class Drink(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    nutrition = models.TextField()
    allergy = models.TextField()
    
    def __str__(self):
        return self.name
    
    
    
class Image(models.Model):
    name = models.ForeignKey('Drink', on_delete=models.CASCADE)
    url = models.URLField(max_length=256)
    
    def __str__(self):
        return str(self.name)
    

    
    

    
