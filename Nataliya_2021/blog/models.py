from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modifield = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='post')

class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


# Create your models here.
