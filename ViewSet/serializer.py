from rest_framework import serializers
from .models import programmer_model

class Programmer_serializer(serializers.Serializer):

    class Meta: 

        model = programmer_model
        fields=('name', 'description')