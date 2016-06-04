from django.db import models
#  from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title
