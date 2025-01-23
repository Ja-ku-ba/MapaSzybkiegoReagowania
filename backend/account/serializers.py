from rest_framework import serializers
from django.core.validators import validate_email

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            email = validate_email(email)
            if CustomUser.objects.filter(email=email).exists():
                raise ValueError('Email already exists')
            return email
        except:
            return ValueError('Invalid email')
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValueError('Username already exists')
        return username
    
    def create(self, validated_data):
        return super().create(validated_data)