from django.db import models
from django_currentuser.db.models import CurrentUserField

class Topic(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    author = CurrentUserField()
    description = models.CharField(max_length=60)
    urlname = models.SlugField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

