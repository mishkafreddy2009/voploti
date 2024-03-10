from django.db import models
from django.core.files import File

from io import BytesIO
from pytils.translit import slugify
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

class Size(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(Size, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image_main = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_image_main(self):
        if self.image_main:
            return self.image_main.url
        return 'https://via.placeholder.com/700'

    def get_image_2(self):
        if self.image_2:
            return self.image_2.url
        return 'https://via.placeholder.com/700'

    def get_image_3(self):
        if self.image_3:
            return self.image_3.url
        return 'https://via.placeholder.com/700'

    def get_image_4(self):
        if self.image_4:
            return self.image_4.url
        return 'https://via.placeholder.com/700'

    def get_image_5(self):
        if self.image_5:
            return self.image_5.url
        return 'https://via.placeholder.com/700'

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        self.alt_image.delete(save=False)
        self.thumbnail.delete(save=False)
        self.alt_thumbnail.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]