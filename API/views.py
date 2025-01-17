from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializer

class HelloAPI(APIView):

    def get(self,request, format= None):

        data =[
                'Se va a utilizar todos los metodos',
                'lslslss',
                'dsaddsd'
        ]

        return Response({"message":"Successful", 'an_apiview':data})
    
    def post(self, request, format = None):

        serialized_data = serializer.programming_serializer(data = request.data)

        if serialized_data.is_valid():

            name = serialized_data.validated_data.get('name')
            message = {"hola {0}".format(name)}

            return Response({"message":message})
        
        return Response({"error": status.HTTP_400_BAD_REQUEST})