from rest_framework import serializers

from message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'message',
        )


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'identificator',
        )
