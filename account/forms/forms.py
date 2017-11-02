from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from cafe.models import Cafe


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2', 'captcha' )

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=30)

class CafeRegistrationForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, help_text='Required.')
    description = forms.CharField(max_length=30,  help_text='Optional.')
    longitude = forms.CharField(max_length=30, required=True, help_text='Required.')
    latitude = forms.CharField(max_length=30, required=True, help_text='Required.')
    main_image_url = forms.CharField(max_length=30, required=True, help_text='Required.')

    class Meta:
        model = Cafe
        fields = ('name', 'description', 'longitude', 'latitude', 'main_image_url' )
