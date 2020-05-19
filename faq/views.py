from django.shortcuts import render


def frequently_asked_view(request):
    return render(request, "frequently_asked.html", {"page_title": "FAQ | PrintCrate"})
