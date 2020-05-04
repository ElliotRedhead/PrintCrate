from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    contact_message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            "rows": 6,
        }),
    )

    class Meta:
        fields = ["subject", "email", "contactmessage"]
