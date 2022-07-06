from django.conf import settings 
from django.contrib.auth import get_user_model 

from rest_framework.authentication import TokenAuthentication 

import jwt

class CustomTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer' 

    def authenticate_credentials(self, token):
        User = get_user_model() 
        JWT_SECRET_KEY = getattr(settings, 'JWT_SECRET_KEY', 'None') 
        JWT_ALGORITHMS = getattr(settings, 'JWT_ALGORITHMS', 'None') 
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITHMS)
        user = User.objects.get(username=payload['user']) 
        user = User.objects.get(username='admin') 
        print('here')   
        return (user, token)

