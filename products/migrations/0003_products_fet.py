# Generated by Django 4.0.3 on 2022-04-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='fet',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
