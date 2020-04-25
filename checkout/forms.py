from django import forms
from .models import CustomerShipping


class CustomerShippingForm(forms.ModelForm):
    class Meta:
        model = CustomerShipping
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
