from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is the accounts index.")
