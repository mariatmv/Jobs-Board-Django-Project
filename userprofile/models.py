from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)


User.userprofile = property(lambda x:UserProfile.objects.get_or_create(user=x)[0])