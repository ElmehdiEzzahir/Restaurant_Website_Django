# Generated by Django 4.0.3 on 2022-05-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_comment_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_showen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='fname',
            field=models.CharField(blank=b'I01\n', max_length=50),
        ),
    ]
