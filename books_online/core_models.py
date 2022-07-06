from tabnanny import verbose
from django.db import models 
from django.utils.translation import gettext_lazy as _ 

import uuid


class TimeStampedModel(models.Model): 
    created_at = models.DateTimeField( 
        verbose_name=_('This is Added at'), 
        help_text=_('This is created at'), 
        auto_now_add=True, 
        null=False, 
        blank=False, 
        editable=False, 
    )

    modified_at = models.DateTimeField( 
        verbose_name=_('Modified at'), 
        help_text=_('Modified at'), 
        auto_now=True, 
        null=False, 
        blank=False, 
        editable=False, 
    )

    class Meta: 
        abstract = True 
    
class UUIDFieldModel(models.Model): 
    id = models.UUIDField( 
        primary_key=True, 
        null=False, 
        blank=False, 
        editable=False, 
        default=uuid.uuid4, 
    )

    class Meta: 
        abstract = True 

class TimeStampedModelUUIDFieldModel(UUIDFieldModel, TimeStampedModel):
    class Meta: 
        abstract = True 

