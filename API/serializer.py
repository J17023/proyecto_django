from rest_framework import serializers

class programming_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    position = serializers.CharField(max_length=30)
    hire_date = serializers.DateField(default= remove_date_offset)