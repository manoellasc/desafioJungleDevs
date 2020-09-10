from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import TopicSerializer
from .models import Topic
from settings.permissions import IsOwnerOrReadOnly
from rest_framework import permissions


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

    def list(self, request,):
        queryset = Topic.objects.filter()
        Topic.author = self.request.user
        serializer = TopicSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Topic.objects.filter()
        Topic.author = self.request.user
        topic = get_object_or_404(queryset, pk=pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]