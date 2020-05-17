from django.shortcuts import render


def about_us(request):
    """
    Renders the "About Us" page.
    """
    return render(request, "about.html", {"page_title": "About | PrintCrate"})
