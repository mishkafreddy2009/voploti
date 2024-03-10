# Generated by Django 5.0.2 on 2024-03-03 13:44

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_customer_options_customer_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='device',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
