# Generated by Django 5.0.2 on 2024-03-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_size_product_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
