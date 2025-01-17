from django.shortcuts import render
from rest_framework import viewsets
from .models import programmer_model
from .serializer import Programmer_serializer

class programmer_viewset(viewsets.ViewSet):
    queryset = programmer_model.objects.all()
    serializer_class = Programmer_serializer