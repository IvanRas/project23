from django.shortcuts import render, get_object_or_404

from catalog.models import Product

# Create your views here.


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def catalog(request):
    return render(request, 'catalog/catalog.urls')


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'product/info_index.html', context=context)


