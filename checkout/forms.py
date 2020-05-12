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


class PaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 12+1)]
    YEAR_CHOICES = [(i, i) for i in range(2017, 2036)]

    credit_card_number = forms.CharField(
        label="Credit card number",
        required=False
    )
    cvv = forms.CharField(
        label="Security code (CVV)",
        required=False
    )
    expiry_month = forms.ChoiceField(
        label="Month", choices=MONTH_CHOICES, required=False
    )
    expiry_year = forms.ChoiceField(
        label="Year", choices=YEAR_CHOICES, required=False
    )
    stripe_id = forms.CharField(widget=forms.HiddenInput())
