from django.db import models
import os
from django.db.models import Q
from eshop_products_categories.models import ProductCategory
from django.contrib.auth.models import User


# =============================== Image Name Generator ===============================
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"


# =============================== Product Manager ===============================
class ProductsManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_product_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id, active=True)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(categories__url__iexact=category_name, active=True)

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()

# =============================== Product Model ===============================
class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    color = models.CharField(max_length=10, verbose_name='Color', default='Black')

    choices = (
        ('Small', 'Small'),
        ('Large', 'Large'),
        ('XL', 'XL'),
        ('XXL', 'XXL')
    )
    size = models.CharField(max_length=10, choices=choices, default='Large', verbose_name='Size')
    before_price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_image_path, default=False, blank=False)
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='Category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    objects = ProductsManager()

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"


# =============================== Product Gallery Model ===============================
class ProductGallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_gallery_image_path, default=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.Case)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'


# =============================== Product Comment ===============================
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.user} on {self.product}'


