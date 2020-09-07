from django.db import models
from topics.models import Topic


class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

