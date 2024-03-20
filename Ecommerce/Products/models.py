from django.db import models

# Create your models here.

class Registration(models.Model):
    companyName =models.CharField(max_length=100)
    ownerName = models.CharField(max_length=100)
    rollNo=models.IntegerField(unique=True)
    ownerEmail=models.EmailField()
    accessCode=models.CharField(max_length=100)

class ProductDetails(models.Model):
    companyName =models.CharField(max_length=100)
    productName = models.CharField(max_length=100)
    price=models.FloatField()
    rating=models.FloatField()
    discount=models.IntegerField()
    availability=models.CharField(max_length=100)