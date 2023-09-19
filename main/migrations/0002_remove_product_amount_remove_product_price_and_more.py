# Generated by Django 4.2.5 on 2023-09-19 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='umur',
        ),
        migrations.AddField(
            model_name='product',
            name='jumlah',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='kategori',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
