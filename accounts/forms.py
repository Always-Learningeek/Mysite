from django.forms import ModelForm
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
#from django.contrib.auth.forms import AuthenticationForm


class LoginForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'password']


class CustomAuthenticationForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user