from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    ADMIN=('Admin','admin')
    SELLER=('Seller','seller')
    CUSTOMER=('Customer','customer')
    VIEWER=('Viewer','viewer')

class CustomUser(AbstractUser):
    role=models.CharField(choices=Role,default=Role.VIEWER)
    phone=models.CharField(max_length=13,blank=True,null=True)
    age=models.PositiveIntegerField(blank=True,null=True)

