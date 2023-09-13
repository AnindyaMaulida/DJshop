from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Name': 'Anindya Maulida Widyatmoko',
        'Kelas': 'PBP A',
        'Description' : 'Kami menyediakan produk berkualitas tinggi dengan harga terjangkau sesuai kebutuhan Anda',
        'Produk': ['Sweater', 'Kaos', 'Jaket', 'Kemeja'],
        'Alamat' : 'Jl. Margonda, Depok',
        'Email': 'DJShop@tokobagus.com',
        'Telepon' : '012345678'

    }

    return render(request, "main.html", context)