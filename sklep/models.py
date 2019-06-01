from django.db import models

# Create your models here.


class Product(models.Model):
    price = models.FloatField()
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    content = models.TextField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


# class Payment(models.Model):
#     Payment_type = models.IntegerField()
#

class Order(models.Model):
    order_number = models.IntegerField()
    user = models.TextField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.FloatField()
    //Payment_type = models.ForeignKey(Payment, on_delete=models.CASCADE)


# class Category(models.Model):
#     category_name = models.IntegerField()
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#
# class ProductType(models.Model):
#     Type = models.IntegerField()
#     Color = models.TextField()
