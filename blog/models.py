from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here


#Category model

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    url = models.CharField(max_length=150)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.title

#Post Model

class Post(models.Model):
    Post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')


    def __str__(self):
        return self.title


class Contact(models.Model):
    s_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    state = models.CharField(max_length=200)
    subject = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name