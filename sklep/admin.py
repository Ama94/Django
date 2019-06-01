from django.contrib import admin
from .models import Product, Review, Order

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['content']

@admin.register(Order)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = [ 'order_number','product_id','user','price','count']