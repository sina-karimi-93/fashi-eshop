from django.db import models


# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    url = models.CharField(max_length=150, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'Product Category'
        verbose_name_plural= 'Product Categories'
