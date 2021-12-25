from rest_framework import serializers
from taskmanager.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')
        model = Post