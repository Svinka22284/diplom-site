import re

from django import forms

class CreateOrderForm(forms.Form):

     first_name = forms.CharField()
     last_name = forms.CharField()
     number = forms.CharField()
     requires_delivery = forms.ChoiceField(
          choices=(
               ("0", "Самовивіз"),
               ("1", "Доставка"),
          )
     )
     delivery_address = forms.CharField(required=False)
     payment_on_get = forms.ChoiceField(
          choices=(
               ("0", "Карткою"),
               ("1", "Готівкою"),
          )
     )

     def clean_phone_number(self):
          data = self.cleaned_data['number']
          if not data.isdigit():
               raise forms.ValidationError("Номер телефону повинен мати тільки цифри")


          pattern = re.compile(r'^\d{10}$')
          if not pattern.match(data):
               raise forms.ValidationError("Незрозумілий формат номеру")

          return data




    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': "Введіть ваше ім'я",
    #
    #         }
    #     )
    # )
    #
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': "Введіть ваше прізвище",
    #         }
    #     )
    # )
    #
    # number = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': "Введіть ваше прізвище",
    #         }
    #     )
    # )
    #
    # requires_delivery = forms.BooleanField(
    #     widget=forms.RedioSelect(
    #         choices=[
    #             ("0",False),
    #             ("1",True),
    #         ],
    #         initial = 0,
    #     )
    # )
    #
    # delivery_address = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'form-control',
    #             'id': 'delivery_address',
    #             'rows': 2,
    #             'placeholder': "Введіть вашу адресу"
    #         }
    #     ),
    #     required=False,
    # )
    #
    # payment_on_get = forms.ChoiceField(
    #     widget=forms.RadioSelect(
    #         choices=[
    #             ("0",False),
    #             ("1",True),
    #         ],
    #         initial="card",
    #     )
    # )