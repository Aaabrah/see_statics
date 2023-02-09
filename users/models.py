from django.db import models

from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    user_image = models.ImageField(upload_to='users/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, default='+998 ')
    following = models.IntegerField(default=0)
    # accept_conditions = models.BooleanField(default=False)

