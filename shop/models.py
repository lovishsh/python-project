from contextlib import nullcontext
from distutils.command.upload import upload
import email
import numbers
from re import T
from tkinter import N
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
 


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=122,null=True)
    category = models.CharField(max_length=122,null=True)
    subcategory = models.CharField(max_length=122,null=True)
    desc= models.CharField(max_length=122,null=True)
    price=models.IntegerField(null=True)
    publishDate=models.DateField(null=True)
    image=models.ImageField(upload_to="shop/images",null=True)

    def __str__(self):
     return self.product_name


class Contact(models.Model):
    name=models.CharField(max_length=255,null=True) 
    email=models.CharField(max_length=255,null=True) 
    password=models.CharField(max_length=255,null=True) 
    number=models.CharField(max_length=255,null=True) 

     
    def __str__(self):
     return self.name

class Order(models.Model):
   
    order_name=models.CharField(max_length=122,null=True)
    email=models.CharField(max_length=122,null=True)
    address1=models.CharField(max_length=122,null=True)
    address2=models.CharField(max_length=122,null=True)
    city=models.CharField(max_length=122,null=True)
    state=models.CharField(max_length=122,null=True)
    zip=models.CharField(max_length=133,null=True)
    number=models.CharField(max_length=133,null=True)
    

    def __str__(self):
     return self.order_name

 