from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from pkg_resources import require

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
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
        username= forms.CharField(
            widget=forms.TextInput(attrs={"class": "input-box",
                                          "placeholder":"username"})
        )
        first_name = forms.CharField(
            widget=forms.TextInput(attrs={"class": "input-box",
                                          "placeholder": "first_name"})
        )
        email = forms.CharField(
            widget=forms.TextInput(attrs={"class": "input-box",
                                          "placeholder": "email"})
        )
        number = forms.CharField(
            widget=forms.TextInput(attrs={"class": "input-box",
                                          "placeholder": "number"})
        )
        password1 = forms.CharField(
            widget=forms.TextInput(attrs={"class": "input-box",
                                          "placeholder": "password"})
        )
        password2 = forms.CharField(
            widget=forms.TextInput(attrs={"class": "input-box",
                                          "placeholder": "confirmation password"})
        )

        class Meta:
            model = User
            fields = ('username',
                      'first_name',
                      'email',
                      'number',
                      'password1',
                      'password2',)

        def save(self, commit=True):
            user = super().save(commit=False)

            user.number = self.cleaned_data['number']

            if commit:
                user.save()

            return user

class ProfileForm(UserChangeForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "from-control mt-3",}),
        required = False
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control",
                                      "placeholder": "Ведіть ваш логін",})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control",
                                      "placeholder": "Ведіть ваше ім'я"})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "form-control",
                                       "placeholder": "Ведіть вашу електрону адресу",})
    )
    number = forms.CharField(
        widget=forms.NumberInput(attrs={"class": "form-control",
                                        "placeholder": "Ведіть ваш номер телефону"})
    )
    class Meta:
        model = User
        fields = ('image',
                  'username',
                  'first_name',
                  'email',
                  'number',)