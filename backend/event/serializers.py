import random

from rest_framework import serializers

from .models import Event
from account.models import CustomUser


C_HUNDRET_M_ON_MAP = 0.001455

class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "latitiude", "longitude", "creator", "type", "description", 
            "show_description" 
        ]
    
        
class EventsMarekrsSerializer(serializers.ModelSerializer):
    latitiude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()
    creator = serializers.SerializerMethodField()
    
    desc = serializers.SerializerMethodField() 
    class Meta:
        model = Event
        fields = [
            "latitiude", "longitude", "creator", "type", "desc", "created_at"
        ]

    def get_desc(self, obj):
        if obj.show_description:
            return obj.description
        return None
    
    def get_latitiude(self, obj):
        randomizer = random.uniform(0, C_HUNDRET_M_ON_MAP)
        return obj.latitiude + randomizer
    
    def get_longitude(self, obj):
        randomizer = random.uniform(0, C_HUNDRET_M_ON_MAP)
        return obj.longitude + randomizer
        
    def get_creator(self, obj):
        return obj.creator.username
    

class EventsListSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source='creator.username')
    class Meta:
        model = Event
        fields = [
            'latitiude', 'longitude', 'creator', 'type', 'created_at', 'description',
            'show_description'
        ]