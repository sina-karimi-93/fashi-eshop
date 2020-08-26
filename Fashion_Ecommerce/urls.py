import os
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from .views import home, header, footer, contact_us
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', home),
    path('', include('eshop_accounts.urls')),  # Account
    path('cart/', include('cart.urls', namespace='cart')),  # Cart
    path('orders/', include('orders.urls', namespace='orders')),  # Order
    path('', include('eshop_products.urls')),   # Product
    path('contact-us', contact_us),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + \
                  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
                  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
