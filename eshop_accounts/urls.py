from django.urls import path
from .views import login_page, register_page, logout_page,user_profile


urlpatterns = [
    path('login/', login_page),
    path('register/', register_page),
    path('logout/', logout_page),
    path('profile/', user_profile),
]
