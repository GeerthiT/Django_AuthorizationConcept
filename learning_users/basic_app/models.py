from django.db import models
from django.contrib.auth.models import User #built in model

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User) #(username, firstname, lastname already included)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self) -> str:
        return self.user.username