from django.conf import settings
from django.db import models

# Create your models here.
class Label(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    discount_price = models.FloatField(blank=True, null=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    labels = models.ForeignKey(Label, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.product.title} ({self.quantity})"


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)

    def __str__(self) -> str:
        return self.user.username
