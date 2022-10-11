from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ads")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ads_images', null=True, blank=True)


class Comment(models.Model):
    text = models.CharField(max_length=200, null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
