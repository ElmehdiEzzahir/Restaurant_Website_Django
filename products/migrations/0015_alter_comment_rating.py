# Generated by Django 4.0.3 on 2022-05-05 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.FloatField(),
        ),
    ]