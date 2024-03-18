# from django.db import models

# # Create your models here.
# class Product(models.Model):
#     name=models.CharField(max_length=50)
#     image=models.CharField(max_length=100)
# class ProductVariant(models.Model):
#     sku=models.CharField(max_length=50)
#     name=models.CharField(max_length=50)
#     details=models.CharField(max_length=50)
#     price=models.DecimalField(max_digits=10,decimal_places=2)
#     product=models.ForeignKey(Product, related_name='variants',on_delete=models.CASCADE,null=False)


# # Example: Print the author's name
    
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=100)

class ProductVariant(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE, null = True)

