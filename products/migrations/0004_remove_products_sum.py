# Generated by Django 4.0.3 on 2022-04-17 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_fet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='sum',
        ),
    ]
