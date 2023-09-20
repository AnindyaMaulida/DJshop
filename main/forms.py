from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
<<<<<<< HEAD
        fields = ["name", "jumlah", "kategori", "description"]
=======
        fields = ["Name", "Jumlah", "Description"]
>>>>>>> 7c04502 (push Tugas 3)
