from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

class MainView(APIView):
    def get(self, request):
        data='data'
        return Response(data)
