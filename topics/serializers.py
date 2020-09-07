from rest_framework import serializers
from .models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name', 'title', 'author', 'description', 'urlname', 'created_at', 'updated_at')

