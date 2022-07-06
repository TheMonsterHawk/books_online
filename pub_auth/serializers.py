from rest_framework import serializers 

from pub_auth.models import Publisher, Author 

class PublisherSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Publisher 
        fields = '__all__' 

class AuthorSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Author 
        fields = '__all__' 
