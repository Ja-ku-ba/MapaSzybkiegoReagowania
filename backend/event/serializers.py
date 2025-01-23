from rest_framework import serializers

from .models import Event
from account.models import CustomUser


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "latitiude", "longitude", "creator", "approved", "banned", "type", 
            "created_at", "updated_at", "description", "show_description", 
        ]
        
    def validate(self, attrs):
        print(attrs)
        return super().validate(attrs)