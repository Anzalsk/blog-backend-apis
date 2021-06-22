from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=180)
    content = models.TextField()
    author = models.ForeignKey(
        to=User,  on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    cover_img = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id', ]

    def __str__(self):
        return str(self.title)
