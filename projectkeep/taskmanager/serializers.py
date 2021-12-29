from rest_framework import serializers
from taskmanager.models import Post,Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'category', 'author', 'excerpt', 'content', 'status')
        model = Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name',)
        model = Category