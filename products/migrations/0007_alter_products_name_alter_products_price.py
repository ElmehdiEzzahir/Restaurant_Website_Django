# Generated by Django 4.0.3 on 2022-04-17 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category_remove_products_fet_remove_products_pric_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=50),
        ),
    ]
