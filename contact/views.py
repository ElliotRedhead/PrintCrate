import os
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_us(request):
    """Constructs email from form, sending details via SMTP.

    If the user is logged in, the email address field is pre-populated.
    Invalid field submission results in user feedback through form validation.
    As content is sent through Gmail SMTP the sender's email address is also included
    in the message body, as the "from" field is overwritten by Gmail account owner's credentials.
    Core code adapted from: https://learndjango.com/tutorials/django-email-contact-form
    Insertion of existing user email adapted from https://stackoverflow.com/a/28374362/
    """
    if request.method == "GET":
        contact_form = ContactForm()
        current_user = request.user
        if str(current_user) != "AnonymousUser":
            contact_form.fields["email"].widget.attrs.update({
                "value": current_user.email
            })
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data["subject"]
            customer_email_address = contact_form.cleaned_data["email"]
            contact_message = customer_email_address + " - " + \
                contact_form.cleaned_data["contact_message"]
            try:
                send_mail(subject, contact_message, customer_email_address, [
                    os.environ.get("EMAIL_RECIPIENT")])
            except BadHeaderError:
                # Prevents header injection.
                return HttpResponse("Invalid header found.")
            except Exception:
                return HttpResponse(f"An exception occurred, please contact site owner with reference: {Exception}")
            return redirect("contact_success")
    return render(
        request,
        "contact.html",
        {"page_title": "Contact Us | PrintCrate", "contact_form": contact_form},
    )


def contact_success(request):
    """Page rendered upon successful contact form submission."""
    return render(
        request,
        "contact_success.html",
        {"page_title": "Contact Success | PrintCrate"}
    )
