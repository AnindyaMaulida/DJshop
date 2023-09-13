from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=255)
    Kelas = models.CharField(max_length=255)
    Produk = models.IntegerField()
    Alamat = models.TextField()
    Telepon = models.TextField()
    Description = models.TextField()
    Email = models.TextField()