# Generated by Django 5.0.2 on 2024-03-02 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
