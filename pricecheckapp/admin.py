from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
      list_display    = ['id','title', 'price','prodcut_url', 'model_number' ,'created_at','product_image_url','brand','rating','categories']

admin.site.register(Product, ProductAdmin)