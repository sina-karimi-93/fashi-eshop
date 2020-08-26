from django.contrib import admin

# Register your models here.
from eshop_products.models import Product, ProductGallery, Comment

admin.site.register(ProductGallery)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'product', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('body',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'active', 'price', 'image')
    list_display_links = ('id', 'title')
    list_editable = ( 'price', 'active')