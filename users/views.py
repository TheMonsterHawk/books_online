from django.shortcuts import render
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth import get_user_model 
from django.conf import settings 

from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly 
from rest_framework.authentication import TokenAuthentication 
from rest_framework.decorators import action 


from users.models import User 
from users.authentication import CustomTokenAuthentication 
from users.serializers import UserSerializer


import jwt 

JWT_ALGORITHMS = getattr(settings, 'JWT_ALGORITHMS', []) 
JWT_SECRET_KEY = getattr(settings, 'JWT_SECRET_KEY', '') 

class UserViewSet(ModelViewSet): 
    queryset = get_user_model().objects.all() 
    authentication_classes = [CustomTokenAuthentication, ]
    permission_classes = [AllowAny, ]
    serializer_class = UserSerializer

    @action(detail=False, methods=['GET'], url_path='all', url_name='all')
    def list_users(self, request): 
        a = User.objects.all()
        return Response(list([str(user)  for user in a]))    

class SignUpView(APIView):
    authentication_classes = list() 
    permission_classes = [AllowAny, ] 

    def get(self, request):
        return Response({
            'message': 'Enter username, email, password to create account!', 
        })

    def post(self, request):
        User = get_user_model() 

        username = request.data.get('username', '') 
        password = request.data.get('password', '') 
        email = request.data.get('email', '') 
        User.objects.create_user(username=username, password=password, email=email) 

        return Response({
            'username': username, 
            'email': email, 
            'password': password, 
        })

class LoginView(APIView):
    authentication_classes = [] 
    permission_classes = [AllowAny, ]

    def get(self, request): 
        response = Response({ 
            'message': 'Enter username and password to login!', 
        })
        response.set_cookie('Authorization', 'Token abc') 
        return response 

    def post(self, request):
        
        User = get_user_model() 
        print(dir(request))     

        username = request.data.get('username', '') 
        password = request.data.get('password', '') 
        try:
            user = User.objects.get(username=username) 
            if user.check_password(password): 
                jwt_encoded = jwt.encode({'user': username}, JWT_SECRET_KEY, algorithm=JWT_ALGORITHMS[0])
                response = Response({
                    'username': username, 
                    'password': password, 
                    'message': f'Welcome back {username}!'
                })
                response.headers['Authorization'] = 'Bearer ' + jwt_encoded 
                response.set_cookie('Authorization', 'Bearer ' + jwt_encoded) 
                return response
            raise Exception('Check your password!') 
        except Exception as err:
            return Response({
                'message': str(err) 
            })
            