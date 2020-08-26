from django.db import models
from eshop_products.models import Product


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    product = models.ManyToManyField(Product, blank=True, verbose_name='Products')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name: 'Tag'
        verbose_name_plural: 'Tags'
