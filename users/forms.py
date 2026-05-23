from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',

        widget=forms.TextInput(attrs={"autofocus": True,
                                      "class": "input-box",
                                      "placeholder": "username"}),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={"autocomplete":"current-password",
                                                                 'class': 'input-box',
                                                                 'placeholder': 'password'}))
    class Meta:
        model = User
        fields = ('email', 'password')