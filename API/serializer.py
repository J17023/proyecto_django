from rest_framework import serializers

class programming_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)