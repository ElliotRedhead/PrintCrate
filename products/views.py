from django.shortcuts import render
from .models import product

def products_view(request):
	products = product.objects.all()
	return render(request, "productslist.html", {"products": products})
