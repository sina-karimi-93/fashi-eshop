# Generated by Django 3.0.8 on 2020-08-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_accounts', '0005_userprofile_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]