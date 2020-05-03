from django.shortcuts import render


def contact_us(request):
    return render(request, "contact.html", {"page_title": "Contact Us | PrintCrate"})
