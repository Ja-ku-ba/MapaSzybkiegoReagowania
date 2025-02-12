from rest_framework import serializers
from email_validator import validate_email as ve

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']
        extra_kwargs = {
                'password': {'write_only': True},
                'email': {'validators': []},
                'username': {'validators': []}
            }

    def validate_email(self, email):
        try:
            email = ve(email, check_deliverability=False)
            email = email.normalized
        except Exception as e:
            raise serializers.ValidationError('Wygląda że chcesz użyć nietypowego adresu email, użyj innego')
        
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email jest zajęty, spróbuj się zalogoawć')
        return email
        
    def validate_username(self, username):
        if CustomUser.objects.filter(username=username).exists():
            raise serializers.ValidationError('Nazwa użytkownika jest zajęta')
        return username
