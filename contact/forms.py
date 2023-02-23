from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(
        required=True,
        label="Subject",
        widget=forms.TextInput(attrs={"placeholder": "Enter Message Subject"}),
    )
    email = forms.EmailField(
        required=True,
        label="Email Address",
        widget=forms.TextInput(
            attrs={"placeholder": "Your Email Address", "autocomplete": "on"}
        ),
    )
    contact_message = forms.CharField(
        required=True,
        label="Contact Message",
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter your contact message here.",
                "rows": 6,
            }
        ),
    )

    class Meta:
        fields = ["subject", "email", "contactmessage"]
