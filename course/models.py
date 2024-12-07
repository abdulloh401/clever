from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='course_img/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.CharField(max_length=30)
    views = models.IntegerField()

    def __str__(self):
        return self.title


class Register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30)
    site = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Event(models.Model):
    img = models.ImageField(upload_to='events_img/')
    date = models.DateTimeField()
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=25)

    def __str__(self):
        return self.name















