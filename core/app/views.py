from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from app.serializers import UserSerializer, AuthTokenSerializer
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    '''Create a new user in the database'''
    serializer_class = UserSerializer

class CreateAuthTokenView(ObtainAuthToken):
    '''Create a token for authenticated user'''
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# Alternative way to create user
# class CreateUserView(APIView):
#     '''Create a new user in the database'''
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             User.objects.create_user(**serializer.data)
#             print(serializer.data)
#         return Response(serializer.data)