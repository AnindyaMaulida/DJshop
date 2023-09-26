from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=255)
    Jumlah = models.IntegerField()
    Description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

