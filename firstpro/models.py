from django.db import models

# Create your models here.
class student(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    

class employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

class register(models.Model):
    Fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact=models.CharField(max_length=10)
    password=models.CharField(max_length=10)

class doc1(models.Model):
    fullname=models.CharField(max_length=100)
    photo=models.FileField(upload_to='images')
