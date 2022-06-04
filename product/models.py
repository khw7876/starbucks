from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=20)
    image = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Drink(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    nutrition = models.TextField()
    allergy = models.TextField()
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

    
    

    
