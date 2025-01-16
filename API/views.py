from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPI(APIView):

    def get(self,request, format= None):

        data =[
                'Se va a utilizar todos los metodos',
                'lslslss',
                'dsaddsd'
        ]

        return Response({"message":"Successful", 'an_apiview':data})
    
    def post(self, request, format = None):

        received_data = request.data

        name = received_data.get('')