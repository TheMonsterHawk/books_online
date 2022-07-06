from django.test import TestCase

from pub_auth.models import Publisher, Author 

class PublisherTest(TestCase): 
    def test_create_publisher(self): 
        publisher = Publisher(name='test') 
        self.assertEqual(publisher.name, 'test') 

class AuthorTest(TestCase): 
    def test_create_author(self): 
        author = Author(name='test') 
        self.assertEqual(author.name, 'test') 
    
