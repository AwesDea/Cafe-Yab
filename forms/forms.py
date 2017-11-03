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
        fields = ('username', 'first_name', 'email', 'password1', 'password2', 'captcha')


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=30)


class CafeRegistrationForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, help_text='Required.')
    description = forms.CharField(max_length=555550, required=False, help_text='Optional.')
    longitude = forms.FloatField(required=True, help_text='Required.')
    latitude = forms.FloatField(required=True, help_text='Required.')
    main_image_url = forms.CharField(max_length=20000, required=True, help_text='Required.')

    class Meta:
        model = Cafe
        fields = ('name', 'description', 'longitude', 'latitude', 'main_image_url')


class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username = forms.CharField(required=False)
    password1 = forms.CharField(required=False, widget=forms.PasswordInput())
    password2 = forms.CharField(required=False, widget=forms.PasswordInput())
    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            self.add_error('password1', 'password error' )

    class Meta:
        model = User
        fields = ('first_name', 'email', 'username', 'password1', 'password2')
