from rest_framework import serializers
from .models import Rooms, Messages, Notification


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = "__all__"

    
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class NotificationReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
        depth = 1