from django.db import models

# Create your models here.
class House(models.Model):
    bhk=models.CharField(max_length=30)
    photo=models.ImageField(upload_to="uploads",default="a.png")
    email=models.EmailField(unique=True)
    owner_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    address=models.CharField(max_length=255)
    place=models.CharField(max_length=255)
    area=models.CharField(max_length=255)



class Login(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)