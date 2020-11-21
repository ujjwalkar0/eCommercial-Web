from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# class layout(models.Model):
#     img1=models.ImageField(upload_to="layout",null=True, blank=True)
#     img2=models.ImageField(upload_to="layout",null=True, blank=True)
#     img3=models.ImageField(upload_to="layout",null=True, blank=True)
#     def get_absolute_url(self):
#         return reverse('home')

class order(models.Model):
    product_id = models.IntegerField(null=True)
    customer_id = models.IntegerField(null=True)
    is_approved = models.BooleanField(default=False,null=True)
    address = models.CharField(max_length=255,null=True,blank=True,)
    quantity = models.IntegerField(null=True)
    def get_absolute_url(self):
        return reverse('home')

class Catagories(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')

class Profile(User):
    image = models.ImageField(null=True,blank=True, upload_to="profile/")
    bio = models.TextField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True,blank=True,)
    mobile_no = models.CharField(max_length=10,null=True,blank=True,)
    website_url = models.CharField(max_length=255,null=True,blank=True,)
    facebook_url = models.CharField(max_length=255,null=True,blank=True,)
    twitter_url = models.CharField(max_length=255,null=True,blank=True,)
    linkdin_url = models.CharField(max_length=255,null=True,blank=True,)

    
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    image = models.ImageField(upload_to="items",null=True, blank=True)
    image2 = models.ImageField(upload_to="items",null=True, blank=True)
    image3 = models.ImageField(upload_to="items",null=True, blank=True)
    image4 = models.ImageField(upload_to="items",null=True, blank=True)
    image5 = models.ImageField(upload_to="items",null=True, blank=True)
    image6 = models.ImageField(upload_to="items",null=True, blank=True)
    stock = models.IntegerField(null=True)
    body = RichTextField(blank=True,null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True,null=True)
    catagory = models.CharField(max_length=50,default='Uncatagories') 
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        # return reverse('article-details',args=(str(self.id)))
        return reverse('home')
