from rest_framework import serializers

from .models import Event
from account.models import CustomUser


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "latitiude", "longitude", "creator", "type", "description", 
            "show_description" 
        ]
        
        
class EventsMarekrsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "latitiude", "longitude", "creator", "type", "description", 
            "show_description" 
        ]
        