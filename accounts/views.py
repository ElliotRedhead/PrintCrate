from django.shortcuts import render


def index(request):
    """Render the accounts index file."""
    return render(request, "index.html")
