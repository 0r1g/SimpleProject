from django.utils import timezone
from datetime import timedelta
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def published_recently(self):
        now = timezone.now()
        return now - timedelta(days=7) <= self.published_date <= now

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
