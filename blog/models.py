from django.db import models
from django.contrib.auth.models import User
from course.models import Category


class Blog(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='blog_img/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
