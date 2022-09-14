from django.shortcuts import render

# TODO: Create your views here.
from katalog.models import CatalogItem

# Create your views here.

def show_katalog(request):
    data_barang_wishlist = CatalogItem.objects.all()
    context = {
    'list': data_barang_wishlist,
    'name': 'Mathilda',
    'id' : '2106751240'
    }
    return render(request, "katalog.html",context)
