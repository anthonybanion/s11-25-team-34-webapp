"""
User Profile and Brand Profile Serializers

File: serializers.py
Author: Anthony Bañon  
Created: 2025-11-29
Last Updated: 2025-11-29
"""
"""
User Profile and Brand Profile Serializers

File: serializers.py
Author: Anthony Bañon  
Created: 2025-11-29
Last Updated: 2025-11-29
"""

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import UserProfile, BrandProfile
from .constants import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password]
    )
    password_confirm = serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField(
        required=False, 
        allow_blank=True, 
        max_length=MAX_PHONE_LENGTH
    )
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'password_confirm', 
            'first_name', 'last_name', 'phone'
        ]
    
    def validate_username(self, value):
        if not value:
            raise serializers.ValidationError("Username is required")
        
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(ERROR_USERNAME_EXISTS)
        return value
    
    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required")
        
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(ERROR_EMAIL_EXISTS)
        return value
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password_confirm": "Passwords do not match"})
        return attrs


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    def validate_username(self, value):
        if not value:
            raise serializers.ValidationError("Username is required")
        return value


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    phone = serializers.CharField(
        required=False, 
        allow_blank=True, 
        max_length=MAX_PHONE_LENGTH
    )
    
    class Meta:
        model = UserProfile
        fields = [
            'username', 'email', 'first_name', 'last_name', 'phone', 
            'eco_points', 'total_carbon_saved', 'is_brand_manager'
        ]
        read_only_fields = ['eco_points', 'total_carbon_saved', 'is_brand_manager']


class BrandProfileSerializer(serializers.ModelSerializer):
    manager_name = serializers.SerializerMethodField()
    manager_email = serializers.SerializerMethodField()
    brand_name = serializers.CharField(max_length=MAX_BRAND_NAME_LENGTH)
    sustainability_story = serializers.CharField(
        required=False, 
        allow_blank=True,
        max_length=MAX_SUSTAINABILITY_STORY_LENGTH
    )
    
    class Meta:
        model = BrandProfile
        fields = [
            'id', 'brand_name', 'sustainability_story', 
            'manager_name', 'manager_email'
        ]
    
    def get_manager_name(self, obj):
        return f"{obj.user_profile.user.first_name} {obj.user_profile.user.last_name}"
    
    def get_manager_email(self, obj):
        return obj.user_profile.user.email
    
    def validate_brand_name(self, value):
        if not value:
            raise serializers.ValidationError("Brand name is required")
        
        if len(value) > MAX_BRAND_NAME_LENGTH:
            raise serializers.ValidationError(
                f"Brand name cannot exceed {MAX_BRAND_NAME_LENGTH} characters"
            )
        return value
    
    def validate_sustainability_story(self, value):
        if value and len(value) > MAX_SUSTAINABILITY_STORY_LENGTH:
            raise serializers.ValidationError(ERROR_STORY_EXCEED_LENGTH)
        return value


class BrandManagerRegistrationSerializer(UserRegistrationSerializer):
    brand_name = serializers.CharField(
        required=True, 
        max_length=MAX_BRAND_NAME_LENGTH
    )
    sustainability_story = serializers.CharField(
        required=False, 
        allow_blank=True,
        max_length=MAX_SUSTAINABILITY_STORY_LENGTH
    )
    
    class Meta(UserRegistrationSerializer.Meta):
        fields = UserRegistrationSerializer.Meta.fields + [
            'brand_name', 'sustainability_story'
        ]
    
    def validate_brand_name(self, value):
        if not value:
            raise serializers.ValidationError("Brand name is required")
        
        if len(value) > MAX_BRAND_NAME_LENGTH:
            raise serializers.ValidationError(
                f"Brand name cannot exceed {MAX_BRAND_NAME_LENGTH} characters"
            )
        
        # Check if brand name already exists
        if BrandProfile.objects.filter(brand_name__iexact=value).exists():
            raise serializers.ValidationError(ERROR_BRAND_NAME_EXISTS)
        return value
    
    def validate_sustainability_story(self, value):
        if value and len(value) > MAX_SUSTAINABILITY_STORY_LENGTH:
            raise serializers.ValidationError(ERROR_STORY_EXCEED_LENGTH)
        return value


class EcoPointsUpdateSerializer(serializers.Serializer):
    points = serializers.IntegerField(required=True)
    carbon_saved = serializers.FloatField(required=False, default=0.0)
    
    def validate_points(self, value):
        if abs(value) > MAX_ECO_POINTS_ADDITION:
            raise serializers.ValidationError(ERROR_POINTS_EXCEED_LIMIT)
        return value
    
    def validate_carbon_saved(self, value):
        if abs(value) > MAX_CARBON_SAVED_ADDITION:
            raise serializers.ValidationError(ERROR_CARBON_EXCEED_LIMIT)
        return value


class BrandStoryUpdateSerializer(serializers.Serializer):
    sustainability_story = serializers.CharField(
        required=True,
        max_length=MAX_SUSTAINABILITY_STORY_LENGTH
    )
    
    def validate_sustainability_story(self, value):
        if not value:
            raise serializers.ValidationError("Sustainability story is required")
        
        if len(value) > MAX_SUSTAINABILITY_STORY_LENGTH:
            raise serializers.ValidationError(ERROR_STORY_EXCEED_LENGTH)
        return value