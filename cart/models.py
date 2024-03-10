import uuid
from django.db import models


COUNTRIES = [('ru', 'Россия')]

class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    country = models.CharField(max_length=255, choices=COUNTRIES, default='ru', verbose_name='Страна')
    email = models.EmailField(max_length=255)
    device = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'