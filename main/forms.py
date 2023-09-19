from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["Name", "Jumlah", "Description"]
<<<<<<< HEAD
=======

>>>>>>> c49b9d5 (Tugas 3 push yaaaaaaz)
