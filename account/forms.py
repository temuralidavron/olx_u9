from django import forms

from account.models import CustomUser, Profile


class RegisterForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=[
            'username',
            'email',
            'age',
            'phone',
            'password'
        ]
    def save(self):
        data=self.cleaned_data
        return CustomUser.objects.create_user(
            username=data.get('username'),
            email=data.get('email'),
            age=data.get('age'),
            phone=data.get('phone'),
            password=data.get('password')
        )

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=50)




class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=[
            'bio',
            'avatar',

        ]