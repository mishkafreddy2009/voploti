# Generated by Django 5.0.2 on 2024-02-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_alt_thubmnail_product_alt_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='alt_image',
            new_name='image_1',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image_2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='alt_thumbnail',
        ),
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_4',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_5',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail_1',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail_2',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail_3',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail_4',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail_5',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
