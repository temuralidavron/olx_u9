# views.py
from http.client import HTTPResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.utils.timezone import now

from config.settings import EMAIL_HOST_USER as from_user
from account.forms import RegisterForm, LoginForm, ProfileForm, ForgetPassword, PasswordDone
from account.models import Profile, CustomUser, Code
from account.utils import sending_email


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


def get_profile(request):
    profile=Profile.objects.get(user=request.user)
    context={
        'profile':profile
    }
    return render(request,'account/profile.html',context)


def update_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form=ProfileForm(instance=profile)

    return render(request,'account/update.html',{'form':form})


# forget password

def forget_password(request):
    if request.method=='POST':
        form=ForgetPassword(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            user=CustomUser.objects.filter(username=username,email=email).first()
            if user:
                code=Code.objects.create(user=user)
                sending_email(
                    to_user=user.email,
                    username=user.username,
                    code=code.code,
                    from_user=from_user

                )
            return render(request,'account/send_email.html')
    form=ForgetPassword()
    return render(request,'account/forget.html',{'form':form})



def password_dane(request):
    username=request.GET.get('name')
    if request.method=='POST':
        form=PasswordDone(request.POST)
        if form.is_valid():
            code_form=form.cleaned_data.get('code')
            password=form.cleaned_data.get('password')
            user=CustomUser.objects.filter(username=username).first()
            if user is None:
                return HTTPResponse("Bunday user mavjud emas")
            code=Code.objects.filter(user=user,code=code_form,allow_time__gt=now()).first()
            print(code.allow_time)
            print("nozirgi varqt",now())
            if code.code==code_form:
                user.set_password(password)
                user.save()
                return redirect("login")

    else:

        form=PasswordDone()

    return render(request,'account/done.html',{'form':form})
~