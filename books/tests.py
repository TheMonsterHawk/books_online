from django.test import TestCase

from books.models import Book 

class BookTest(TestCase): 
    def test_create_book(self): 
        book = Book.objects.create(name='Harry Potter')  
        self.assertEqual(book.name, 'Harry Potter') 
    