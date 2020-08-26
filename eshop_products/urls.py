from django.urls import path
from .views import (ProductList,
                    ProductListByCategory,
                    products_categories_partial,
                    products_tag_partial,
                    SearchProductsView,
                    product_detail)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:productId>/<name>', product_detail, name='product_detail'),
    path('products/search/', SearchProductsView.as_view(), name='search'),
    path('products/category/<category_name>', ProductListByCategory.as_view()),
    path('product_categories_partial', products_categories_partial, name='products_categories_partial'),
    path('products_tag_partial', products_tag_partial, name='products_tag_partial'),

]
