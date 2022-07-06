from sqlite3 import Time
from django.db import models
from django.utils.translation import gettext_lazy as _ 

from books_online.core_models import TimeStampedModel, TimeStampedModelUUIDFieldModel, UUIDFieldModel 

import datetime 
import dateutil 

class Publisher(TimeStampedModelUUIDFieldModel):
    name = models.CharField( 
        max_length=100, 
        verbose_name=_('Publisher\'s Name'),  
        help_text=_('Publisher\'s Name'), 
        null=False, 
        blank=False, 
    )

    class Meta: 
        verbose_name = 'Publisher' 
        verbose_name_plural = 'Publishers' 
        db_table = 'Publisher' 

class Author(TimeStampedModelUUIDFieldModel): 
    name = models.CharField( 
        max_length=100, 
        verbose_name=_('Author'), 
        help_text=_('Author'), 
        null=False,
        blank=False, 
    )

    class Meta: 
        verbose_name = _('Author') 
        verbose_name_plural = _('Authors') 
        db_table = 'Author' 

