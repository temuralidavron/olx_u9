from django.core.exceptions import ValidationError
from django.db import models, transaction
from django.shortcuts import redirect

from account.models import CustomUser


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    create_date = models.DateTimeField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Yetarli mahsulot bormi?
        if self.quantity > self.product.quantity:
            return redirect('product-list')

        # Transaction ichida yozish (xavfsizlik uchun)
        with transaction.atomic():
            self.product.quantity -= self.quantity
            self.product.save()
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} oldi {self.product.title} dan "

