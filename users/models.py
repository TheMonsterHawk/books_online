from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils.translation import gettext_lazy as _ 
from django.core.exceptions import  ValidationError

import datetime 
import dateutil 

from books_online.core_models import TimeStampedModelUUIDFieldModel, UUIDFieldModel

GENDER_OPTIONS = ( 
    ('wont-say', 'Won\'t Say'), 
    ('female', 'Female'), 
    ('male', 'Male'), 
)

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



