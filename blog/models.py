from django.db import models
#  from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=128)
    date_published = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.title
