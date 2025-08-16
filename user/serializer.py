from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators = [validate_password], write_only = True, required = True)
    password_two = serializers.CharField(write_only = True, required = True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_two')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_two']:
            raise serializers.ValidationError({'errors': 'Passwords does not match!'})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_two')
        user = User.objects.create_user(**validated_data)
        return user