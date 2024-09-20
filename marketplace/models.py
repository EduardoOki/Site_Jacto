from django.db import models
from django.conf import settings


class ProductCategory(models.Model):
    category = models.TextField(
        null=False
    )
class Product(models.Model):
    name = models.TextField(null=False)

    price = models.FloatField(null=False)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    characteristics = models.TextField(null=True)

    product_type = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )

    description = models.TextField(null=True)

class ProductImages(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to='images'
    )


class ClientType(models.Model):
    type = models.TextField(
        null=False
    )

class Client(models.Model):
    user =  models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        
    type =  models.ForeignKey(ClientType,
    on_delete= models.CASCADE)