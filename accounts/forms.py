from django.forms import ModelForm
from captcha.fields import CaptchaField
from django.contrib.auth.models import User

class LoginForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'password']
