from django.db import models
from posts.models import Post
from django_currentuser.db.models import CurrentUserField


class Comment(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=60)
    author = CurrentUserField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
