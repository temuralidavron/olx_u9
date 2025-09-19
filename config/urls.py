
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('olx.urls')),
    path('accounts/',include('account.urls')),
]
