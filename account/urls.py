from tkinter.font import names

from django.urls import path

from account import views

urlpatterns=[
    path('',views.register_view,name='register'),
    # path('login/',views.login_view,name='login'),
    path('login/', views.my_view, name='login'),
    path('logout/',views.logout_view,name='logout'),

    # profile
    path('profile/',views.get_profile,name='profile'),
    path('profile/update/',views.update_profile,name='profile-update'),

    # forget ps
    path('forget/',views.forget_password,name="forget"),
    path('forget/done/',views.password_dane,name="done"),


]