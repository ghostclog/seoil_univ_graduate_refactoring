from .models import Posts,PostComments
from rest_framework import serializers

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class PostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = '__all__'