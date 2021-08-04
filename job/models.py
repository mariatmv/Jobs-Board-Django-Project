from django.contrib.auth.models import User
from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    long_description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    wage = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    author = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    changed_on = models.DateTimeField(auto_now=True)

    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    contact_name = models.CharField(max_length=50, blank=True, null=True)
    contact_email = models.EmailField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
