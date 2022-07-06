from django.contrib import admin

from pub_auth.models import Publisher, Author 

@admin.register(Publisher) 
class PublisherAdmin(admin.ModelAdmin): 
    pass 

@admin.register(Author) 
class AuthorAdmin(admin.ModelAdmin): 
    pass 

