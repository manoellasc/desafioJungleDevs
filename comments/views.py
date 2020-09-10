from rest_framework import viewsets
from .serializers import CommentSerializer
from .models import Comment
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from settings.permissions import IsOwnerOrReadOnly
from rest_framework import permissions


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def list(self, request, topics_pk=None, posts_pk=None):
        queryset = Comment.objects.filter(post=posts_pk, post__topic__urlname=topics_pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Comment.objects.filter(id=id)
        comment = get_object_or_404(queryset, id=id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]