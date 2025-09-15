# views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from account.forms import RegisterForm, LoginForm


def register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegisterForm()
    return render(request, "account/register.html", {"form": form})


def my_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            print(user)
            if user:
                login(request, user)
                print('keldi')
                return redirect('product-list')
    else:
        form=LoginForm()
    return render(request,'account/my_login.html',{'form':form})


# # Register
# def register_view(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login")
#     else:
#         form = UserCreationForm()
#     return render(request, "account/register.html", {"form": form})
#
# # Login
# def login_view(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("list")
#     else:
#         form = AuthenticationForm()
#     return render(request, "account/login.html", {"form": form})
#
# # Logout
def logout_view(request):
    logout(request)
    return redirect("login")