from django.shortcuts import render


def about_us(request):
    return render(request, "about.html", {"page_title": "About | PrintCrate"})
