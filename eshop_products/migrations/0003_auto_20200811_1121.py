# Generated by Django 3.0.8 on 2020-08-11 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0002_auto_20200810_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
