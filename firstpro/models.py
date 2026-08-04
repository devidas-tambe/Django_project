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

class Author(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=100)
    at=models.ForeignKey(Author,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class admin1(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

    class Meta:
        abstract=True

class customer(admin1):
    c_id=models.CharField(max_length=100)

class seller(admin1):
    s_id=models.CharField(max_length=100)

class child1(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()

    class Meta:
        abstract=True

class parent(child1):
    profile=models.CharField(max_length=100)

class grandparent(child1):
    identity=models.CharField(max_length=100)

class job(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    task=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class work(job):
    class Meta:
        proxy=True
