from .models import Teams,TeamPosts,ChatLog,TeamPostComment
from rest_framework import serializers

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'

class TeamPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPosts
        fields = '__all__'

class ChatLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatLog
        fields = '__all__'

class TeamPostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPostComment
        fields = '__all__'