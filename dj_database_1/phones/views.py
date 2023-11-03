from django.shortcuts import render
from .models import Phone

def index(request):
    return render(request, 'index.html')

def show_catalog(request):
    sort = request.GET.get('sort', 'name')
    if sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.order_by('name')
    return render(request, 'catalog.html', {'phones': phones})

def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    return render(request, 'product.html', {'phone': phone})