from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils.translation import gettext_lazy as _ 
from django.core.exceptions import  ValidationError

import datetime 
from dateutil.relativedelta import relativedelta
import pytz 

from books_online.core_models import TimeStampedModelUUIDFieldModel, UUIDFieldModel

GENDER_OPTIONS = ( 
    ('wont-say', 'Won\'t Say'), 
    ('female', 'Female'), 
    ('male', 'Male'), 
)


# class BookUserData(models.Model): 
#     book = models.ForeignKey(
#         Book, 
#         on_delete=models.CASCADE, 
#         related_name='book_user_meta', 
#         related_query_name='book_user_meta', 
#         help_text=_('book'), 
#         null=False, 
#         blank=False, 
#     )

#     user = models.ForeignKey( 
#         User, 
#         on_delete=models.CASCADE, 
#         related_name='book_user_meta', 
#         related_query_name='book_user_meta', 
#         help_text=_('User'), 
#         verbose_name=_('User'), 
#         null=False, 
#         blank=False, 
#     )

#     page_number = models.IntegerField(
#         default=0, 
#         null=False, 
#         blank=False, 
#         verbose_name=_('Last page read'), 
#         help_text=('Page till where you have completed the book'), 
#     )

#     class Meta: 
#         verbose_name = 'BookUserData' 
#         verbose_name_plural = 'BookUserData'
    
#     def __str__(self): 
#         return f'{self.book} of {self.user}' 

class User(AbstractUser, UUIDFieldModel): 
    gender = models.CharField(
        max_length=100, 
        verbose_name=_('Gender'), 
        help_text=_('Gender'), 
        default='wont-say', 
        choices=GENDER_OPTIONS, 
    )

    birth_date = models.DateTimeField( 
        verbose_name=_('Date of birth'), 
        help_text=_('Date of birth'), 
        null=True, 
        blank=True, 
    )

    @property 
    def age(self): 
        timezone = pytz.timezone('Asia/Kolkata')
        d = datetime.datetime.now()
        d = pytz.utc.localize(d) 
        return relativedelta(d, self.birth_date).years  

    @property 
    def name(self): 
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        if self.gender: 
            if self.gender not in ['male', 'female', 'wont-say']: 
                raise ValidationError('Gender value can only be "male", "female" and "wont-say". %s is not allowed.' %self.gender) 

        super(User, self).save(*args, **kwargs) 
    
    def __str__(self): 
        return self.username 
    
    class Meta: 
        db_table = 'User' 
        verbose_name = _('User') 
        verbose_name_plural = _('Users')  
