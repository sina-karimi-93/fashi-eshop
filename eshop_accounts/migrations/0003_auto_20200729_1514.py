# Generated by Django 3.0.8 on 2020-07-29 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_accounts', '0002_auto_20200729_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='avatar',
            new_name='image',
        ),
    ]
