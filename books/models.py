from django.db import models
from django.utils.translation import gettext_lazy as _ 

from books_online.core_models import TimeStampedModelUUIDFieldModel

from pub_auth.models import Publisher, Author 
from users.models import User 

class Book(TimeStampedModelUUIDFieldModel): 
    name = models.CharField( 
        max_length=1000, 
        unique=True, 
        null=False, 
        blank=False, 
        default='', 
        verbose_name=_('Book'), 
        help_text=_('Book'), 
    ) 

    publisher = models.ForeignKey( 
        Publisher, 
        on_delete=models.CASCADE, 
        related_name='books', 
        related_query_name='books', 
        help_text=_('Publisher of the book'), 
        verbose_name=_('Publisher'), 
        default='', 
        blank=True, 
        null=True, 
    )

    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books', 
        related_query_name='books', 
        verbose_name=_('Author'), 
        help_text=_('Author'), 
        default='', 
        blank=True, 
        null=True, 
    )

    added_by_user = models.ForeignKey( 
        User, 
        on_delete=models.CASCADE, 
        related_name='books_added', 
        related_query_name='books_added', 
        help_text=_('Added by user'), 
        verbose_name=_('Added by user'), 
        default='', 
        blank=False, 
        null=True, 
    )

    subscribers = models.ManyToManyField( 
        User, 
        related_name='books_in_inventory', 
        related_query_name='books_in_inventory', 
        help_text=_('List of users who have included this book in their inventory.'), 
        verbose_name=_('Subscribers'), 
    )

    class Meta: 
        verbose_name = _('Book') 
        verbose_name_plural = _('Books') 
        db_table = 'Book' 
    
    def __str__(self):
        return self.name 


