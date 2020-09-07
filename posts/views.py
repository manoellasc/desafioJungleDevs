from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def list(self, request, topics_pk=None):
        queryset = Post.objects.filter(topic__urlname=topics_pk)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, urlname=None):
        queryset = Post.objects.filter(id=id, topic=urlname)
        post = get_object_or_404(queryset, id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)