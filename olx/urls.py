from tkinter.font import names

from django.urls import path

from olx import views

urlpatterns=[
    path('',views.product_list,name='product-list'),
    path('detail/<int:pk>/',views.product_detail,name='product-detail'),
    path('order/<int:pk>/',views.create_order,name='order'),

    #
    path('cats/<int:pk>/',views.get_cat,name='cat-detail'),



]