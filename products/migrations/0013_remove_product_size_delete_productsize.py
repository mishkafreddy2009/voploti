# Generated by Django 5.0.2 on 2024-02-25 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.DeleteModel(
            name='ProductSize',
        ),
    ]
