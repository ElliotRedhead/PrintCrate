from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=True)
    contact_message = forms.CharField(
        widget=forms.Textarea(attrs={
            "rows": 6,
        }),
    )

    class Meta:
        fields = ["name", "email", "contactmessage"]
