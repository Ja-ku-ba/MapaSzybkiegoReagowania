from django.db import models

from account.models import CustomUser
from .constants import C_EVENTS_LIST, C_INTERACTION_LIST


# Create your models here.
class Event(models.Model):
    latitiude = models.FloatField()
    longitude = models.FloatField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    approved = models.BooleanField()
    banned = models.BooleanField()
    type = models.CharField(max_length=4, choices=C_EVENTS_LIST)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=1024)
    show_description = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'event'
        ordering = ('-created_at', '-updated_at')
    
    
class EventInteraction(models.Model):
    type = models.CharField(max_length=4, choices=C_INTERACTION_LIST)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'event_interaction'
        ordering = ('-created_at', '-updated_at')
        
        
class EventProcessing(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'event_processing'
        ordering = ('-created_at',)
