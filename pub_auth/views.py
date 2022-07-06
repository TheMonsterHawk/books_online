from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny 
from rest_framework.authentication import TokenAuthentication
from pub_auth.serializers import PublisherSerializer 

from users.authentication import CustomTokenAuthentication 

from pub_auth.models import Publisher, Author
from pub_auth.serializers import PublisherSerializer, AuthorSerializer 

class PublisherViewSet(ModelViewSet): 
    queryset = Publisher.objects.all() 
    serializer_class = PublisherSerializer 
    permission_classes = [AllowAny]
    authentication_classes = [] 

class AuthorViewSet(ModelViewSet): 
    queryset = Author.objects.all() 
    serializer_class = PublisherSerializer 
    permission_classes = [AllowAny] 
    authentication_classes = [] 

