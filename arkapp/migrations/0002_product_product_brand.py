# Generated by Django 4.1.5 on 2023-09-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arkapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_brand',
            field=models.CharField(default='', max_length=100),
        ),
    ]
