from datetime import datetime, timedelta
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.db import models
import random



class Role(models.TextChoices):
    ADMIN=('Admin','admin')
    SELLER=('Seller','seller')
    CUSTOMER=('Customer','customer')
    VIEWER=('Viewer','viewer')

class CustomUser(AbstractUser):
    role=models.CharField(choices=Role,default=Role.VIEWER)
    phone=models.CharField(max_length=13,blank=True,null=True)
    age=models.PositiveIntegerField(blank=True,null=True)

def create_code():
    num=random.randint(100000,999999)
    return str(num)
def checking_time():
    return timezone.now() + timedelta(minutes=2)
# def checking_time():
#     return datetime.now()+timedelta(minutes=2)



class Code(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='code')
    code=models.CharField(default=create_code)
    allow_time=models.DateTimeField(default=checking_time)



class Profile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='profile')
    avatar=models.ImageField(upload_to='avatar',blank=True,null=True,default='default/kim.jpg')
    bio=models.TextField(blank=True,null=True)


#crud

class Ustudy(models.Model):
    group_count=models.IntegerField()
    description=models.TextField()
