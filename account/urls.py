from django.urls import path

from account import views

urlpatterns=[
    path('',views.register_view,name='register'),
    # path('login/',views.login_view,name='login'),
    path('login/', views.my_view, name='login'),
    path('logout/',views.logout_view,name='logout'),


]