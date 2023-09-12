from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    umur = models.IntegerField()
    amount = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()