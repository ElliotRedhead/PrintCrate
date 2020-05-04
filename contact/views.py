import os
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# https://learndjango.com/tutorials/django-email-contact-form


def contact_us(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            customer_email_address = form.cleaned_data["email"]
            contact_message = form.cleaned_data["contact_message"]
            try:
                send_mail(subject, contact_message, customer_email_address, [
                          os.environ.get("EMAIL_RECIPIENT")])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home")
    return render(
        request,
        "contact.html",
        {"page_title": "Contact Us | PrintCrate", "form": form},
    )
