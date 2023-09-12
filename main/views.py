from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Anindya Maulida Widyatmoko',
        'class': 'PBP A',
        'umur': '17'
    }

    return render(request, "main.html", context)