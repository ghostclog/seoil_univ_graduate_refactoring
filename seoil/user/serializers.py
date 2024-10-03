from .models import Users,Messages,UserItems
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'

class UserItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserItems
        fields = '__all__'