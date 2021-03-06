from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Account

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        exclude = ['date_created', 'user']