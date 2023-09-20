# from django.db import models

# # Create your models here.
# class Product(models.Model):
#     Name = models.CharField(max_length=255)
#     Kelas = models.CharField(max_length=255)
#     Produk = models.IntegerField()
#     Alamat = models.TextField()
#     Telepon = models.TextField()
#     Description = models.TextField()
#     Email = models.TextField()

# main/models.py

import datetime
from django.db import models

class Product(models.Model):
<<<<<<< HEAD
    # Produk = models.IntegerField()

    name = models.CharField(max_length=255)
    jumlah = models.IntegerField()
    kategori = models.CharField(max_length=255)
    description = models.TextField()
    # date_added = models.DateField(auto_now_add=True)
    date_added=models.DateField(default=datetime.date.today().isoformat)



    def __str__(self):
        return self.name
    

=======
    Name = models.CharField(max_length=255)
    Jumlah = models.IntegerField()
    Description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
>>>>>>> 7c04502 (push Tugas 3)
