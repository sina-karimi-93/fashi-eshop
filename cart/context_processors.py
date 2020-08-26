from .cart import Cart
from eshop_products.models import Product


def cart(request):
    return {
        'cart': Cart(request),
    }
