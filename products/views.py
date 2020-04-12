from django.shortcuts import render
from .models import product

def products_view(request):
	return render(request, "productslist.html")
