# Generated by Django 3.0.8 on 2020-07-29 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import eshop_products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eshop_products_categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('color', models.CharField(default='Black', max_length=10, verbose_name='Color')),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Large', 'Large'), ('XL', 'XL'), ('XXL', 'XXL')], default='Large', max_length=10, verbose_name='Size')),
                ('before_price', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(default=False, upload_to=eshop_products.models.upload_image_path)),
                ('active', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(blank=True, to='eshop_products_categories.ProductCategory', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(default=False, upload_to=eshop_products.models.upload_gallery_image_path)),
                ('product', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='eshop_products.Product')),
            ],
            options={
                'verbose_name': 'Product Gallery',
                'verbose_name_plural': 'Product Galleries',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='eshop_products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]