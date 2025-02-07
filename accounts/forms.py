from django.forms import ModelForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class LoginForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = '__all__'