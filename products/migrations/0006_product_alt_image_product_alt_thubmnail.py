# Generated by Django 5.0.2 on 2024-02-19 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='alt_image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='product',
            name='alt_thubmnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
