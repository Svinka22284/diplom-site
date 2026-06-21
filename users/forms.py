import re

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.core.exceptions import ValidationError

from users.models import User

REQUIRED_MSG = "Це поле є обов'язковим."


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логін",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "class": "input-box",
                "placeholder": "Введіть логін",
            }
        ),
        error_messages={"required": "Заповніть усі обов'язкові поля."},
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "input-box",
                "placeholder": "Введіть пароль",
            }
        ),
        error_messages={"required": "Заповніть усі обов'язкові поля."},
    )

    error_messages = {
        "invalid_login": "Невірний логін або пароль.",
        "inactive": "Обліковий запис неактивний.",
    }

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "input-box", "placeholder": "Введіть логін"}
        ),
        error_messages={
            "required": REQUIRED_MSG,
            "unique": "Користувач з таким логіном вже існує.",
        },
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "input-box", "placeholder": "Введіть ім'я"}
        ),
        error_messages={"required": REQUIRED_MSG},
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "input-box", "placeholder": "Введіть електронну пошту"}
        ),
        error_messages={
            "required": REQUIRED_MSG,
            "invalid": "Введіть коректну адресу електронної пошти.",
        },
    )
    number = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "input-box", "placeholder": "Введіть номер телефону"}
        ),
        error_messages={"required": REQUIRED_MSG},
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "input-box", "placeholder": "Введіть пароль"}
        ),
        error_messages={"required": REQUIRED_MSG},
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "input-box", "placeholder": "Підтвердіть пароль"}
        ),
        error_messages={"required": REQUIRED_MSG},
    )

    error_messages = {
        "password_mismatch": "Паролі не співпадають.",
    }

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "email",
            "number",
            "password1",
            "password2",
        )

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")

        if password1 and len(password1) < 8:
            raise ValidationError("Пароль занадто короткий.")

        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.number = self.cleaned_data["number"]
        if commit:
            user.save()
        return user


class ProfileForm(UserChangeForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "from-control mt-3"}),
        required=False,
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ведіть ваш логін"}
        ),
        error_messages={
            "required": REQUIRED_MSG,
            "unique": "Користувач з таким логіном вже існує.",
        },
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ведіть ваше ім'я"}
        ),
        error_messages={"required": REQUIRED_MSG},
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Ведіть вашу електрону адресу"}
        ),
        error_messages={
            "required": REQUIRED_MSG,
            "invalid": "Введіть коректну адресу електронної пошти.",
        },
    )
    number = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ведіть ваш номер телефону"}
        ),
        error_messages={"required": REQUIRED_MSG},
    )

    class Meta:
        model = User
        fields = ("image", "username", "first_name", "email", "number")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "password" in self.fields:
            del self.fields["password"]
