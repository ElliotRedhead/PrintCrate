from django import forms
from .models import OrderDetails


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = [
            "full_name",
            "primary_address_line",
            "secondary_address_line",
            "town_or_city",
            "county",
            "postcode",
            "country",
            "phone_number"
        ]
