from email.policy import default
from django.db import models

class Product(models.Model):
    title = models.TextField(max_length=255)
    price = models.FloatField(max_length = 255)
    model_number = models.CharField(max_length = 120)
    prodcut_url = models.URLField(max_length = 600,null=True,blank=True)
    product_image_url = models.URLField(max_length = 600,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=False)
    brand=models.CharField(max_length = 255 ,null=True,blank=True)
    rating=models.FloatField(max_length=50,null=True,blank=True)

    categories=models.CharField(max_length = 600 ,null=True,blank=True)
    # sub_category=models.CharField(max_length=255,null=True,blank=True)
    # sub_sub_category=models.CharField(max_length=255,null=True,blank=True)
    