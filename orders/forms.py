import re

from django import forms
from django.core.exceptions import ValidationError

REQUIRED_MSG = "Це поле є обов'язковим."


class CreateOrderForm(forms.Form):
    first_name = forms.CharField(
        error_messages={"required": "Вкажіть ім'я отримувача."},
    )
    last_name = forms.CharField(
        error_messages={"required": "Вкажіть прізвище отримувача."},
    )
    number = forms.CharField(
        error_messages={"required": "Вкажіть номер телефону."},
    )
    requires_delivery = forms.ChoiceField(
        choices=(
            ("0", "Самовивіз"),
            ("1", "Доставка"),
        ),
        error_messages={"required": REQUIRED_MSG},
    )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=(
            ("0", "Карткою"),
            ("1", "Готівкою"),
        ),
        error_messages={"required": REQUIRED_MSG},
    )

    def clean(self):
        cleaned_data = super().clean()
        requires_delivery = cleaned_data.get("requires_delivery")
        delivery_address = (cleaned_data.get("delivery_address") or "").strip()

        if requires_delivery == "1" and not delivery_address:
            self.add_error("delivery_address", "Вкажіть адресу доставки.")

        return cleaned_data

    def clean_number(self):
        data = self.cleaned_data.get("number", "")
        if not data:
            raise ValidationError("Вкажіть номер телефону.")
        if not data.isdigit():
            raise ValidationError("Номер телефону повинен містити тільки цифри.")

        pattern = re.compile(r"^\d{10}$")
        if not pattern.match(data):
            raise ValidationError("Номер телефону повинен містити 10 цифр.")

        return data
