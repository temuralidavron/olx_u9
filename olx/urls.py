from django.urls import path

from olx import views

urlpatterns=[
    path('',views.product_list,name='product-list'),



]