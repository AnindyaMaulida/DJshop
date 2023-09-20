from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm, Product
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_main(request):
    products = Product.objects.all()
    context = {
        'Name': 'Anindya Maulida Widyatmoko',
        'Kelas': 'PBP A',
        'Description' : 'Kami menyediakan produk berkualitas tinggi dengan harga terjangkau sesuai kebutuhan Anda',
        'list_produk': ['Sweater', 'Kaos', 'Jaket', 'Kemeja'],
        'Alamat' : 'Jl. Margonda, Depok',
        'Email': 'DJShop@tokobagus.com',
        'Telepon' : '012345678',
        'products': products


    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")    

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")