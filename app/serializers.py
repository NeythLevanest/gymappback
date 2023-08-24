from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers
from datetime import datetime

from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from app.models import *



class UsersSerializer (serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = '__all__'
    def create(self, validate_data):
        """
        Create and return a new user instance, given the validate data
        """
        return UserTable.objects.create(**validate_data)

class UserTypeClientSerializer (serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = ('is_staff','is_superuser')
        
class UserBasicSerializer (serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = ('id', 'first_name', 'last_name')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = ('id', 'email','first_name', 'last_name', 'password')
    
    def create(self, validated_data):
        user = UserTable.objects.create_user(
            #username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user