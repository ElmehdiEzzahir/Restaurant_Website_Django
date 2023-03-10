# from django.db import models

# # Create your models here.
# class products(models.Model):
#     title= models.TextField()
#     desc=models.TextField()
#     pric=models.TextField()
#     img = models.ImageField(upload_to='imgs/',default='imgs/1.jpg')
#     fet= models.BooleanField()
# import email

from pickle import TRUE
from unicodedata import name
from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField


class products(models.Model):
    name = models.CharField(max_length=50) 
    img = models.ImageField(upload_to='imgs/')
    price = models.DecimalField(max_digits=50,decimal_places=3)
    category = models.ManyToManyField('Category',related_name='item')
    # def get_image(self):
    #     if self.img and hasattr(self.img, 'url'):
    #         return self.img.url
    #     else:
    #         return 'static\imgs\1.jpg'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField(
        'products', related_name='order', blank=True)
    namecl=models.CharField(max_length=50,blank=True)
    email=models.CharField(max_length=50,blank=True)
    number=models.CharField(max_length=50,blank=True)
    adressecl=models.CharField(max_length=100,blank=True)
    ispayed=models.BooleanField(default=False)
    isshiped=models.BooleanField(default=False)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'



class comment(models.Model):
    commented_on=models.DateTimeField(auto_now_add=True)
    fname=models.CharField(max_length=50,blank=TRUE)
    email=models.CharField(max_length=50,blank=True)
    rating = models.FloatField()
    gender=models.CharField(max_length=50,blank=True)
    comment=models.CharField(max_length=1000,blank=True)
    is_showen=models.BooleanField(default=False)

    def __str__(self):
        return f'Comment: {self.commented_on.strftime("%b %d %I: %M %p")}'

    
