from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm


from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логін',
        widget=forms.TextInput(attrs={"autofocus": True,
                                      "class": "input-box",
                                      "placeholder": "Введіть логін"}),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={"autocomplete":"current-password",
                                          'class': 'input-box',
                                          'placeholder': 'Введіть пароль'}))
    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
        username= forms.CharField(
            widget=forms.TextInput(attrs={"class": "input-box",
                                          "placeholder": "Введіть логін"})
        )
        first_name = forms.CharField(
            widget=forms.TextInput(attrs={"class": "input-box",
                                          "placeholder": "Введіть ім'я"})
        )
        email = forms.CharField(
            widget=forms.TextInput(attrs={"class": "input-box",
                                          "placeholder": "Введіть електронну пошту"})
        )
        number = forms.CharField(
            widget=forms.TextInput(attrs={"class": "input-box",
                                          "placeholder": "Введіть номер телефону"})
        )
        password1 = forms.CharField(
            widget=forms.TextInput(attrs={"class": "input-box",
                                          "placeholder": "Введіть пароль"})
        )
        password2 = forms.CharField(
            widget=forms.TextInput(attrs={"class": "input-box",
                                          "placeholder": "Підтвердіть пароль"})
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