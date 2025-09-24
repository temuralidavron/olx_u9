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




class Profile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='profile')
    avatar=models.ImageField(upload_to='avatar',blank=True,null=True,default='default/kim.jpg')
    bio=models.TextField(blank=True,null=True)


