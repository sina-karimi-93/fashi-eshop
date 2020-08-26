from django.db import models
from django.conf import settings


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='Avatars', default='default.png')
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} Profile'
