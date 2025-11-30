"""
User Profile and Brand Profile Views

File: views.py
Author: Anthony Bañon
Created: 2025-11-29
Last Updated: 2025-11-29
"""

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import (
    UserRegistrationSerializer, 
    UserLoginSerializer,
    UserProfileSerializer,
    BrandProfileSerializer,
    BrandManagerRegistrationSerializer,
    EcoPointsUpdateSerializer,
    BrandStoryUpdateSerializer
)
from .services import auth_service, user_profile_service, brand_profile_service
from .constants import *
from .services import BusinessException


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """
    Register a new regular user
    """
    serializer = UserRegistrationSerializer(data=request.data)
    
    if serializer.is_valid():
        try:
            user_data = {
                'username': serializer.validated_data['username'],
                'email': serializer.validated_data['email'],
                'password': serializer.validated_data['password'],
                'first_name': serializer.validated_data.get('first_name', ''),
                'last_name': serializer.validated_data.get('last_name', '')
            }
            
            profile_data = {
                'phone': serializer.validated_data.get('phone', '')
            }
            
            result = auth_service.register_user(user_data, profile_data)
            return Response({
                'message': SUCCESS_REGISTRATION,
                'data': result
            }, status=status.HTTP_201_CREATED)
            
        except BusinessException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_brand_manager(request):
    """
    Register a new brand manager user
    """
    serializer = BrandManagerRegistrationSerializer(data=request.data)
    
    if serializer.is_valid():
        try:
            user_data = {
                'username': serializer.validated_data['username'],
                'email': serializer.validated_data['email'],
                'password': serializer.validated_data['password'],
                'first_name': serializer.validated_data.get('first_name', ''),
                'last_name': serializer.validated_data.get('last_name', '')
            }
            
            brand_data = {
                'brand_name': serializer.validated_data['brand_name'],
                'sustainability_story': serializer.validated_data.get('sustainability_story', '')
            }
            
            result = user_profile_service.create_brand_manager(user_data, brand_data)
            return Response({
                'message': SUCCESS_REGISTRATION,
                'data': result
            }, status=status.HTTP_201_CREATED)
            
        except BusinessException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """
    User login
    """
    serializer = UserLoginSerializer(data=request.data)
    
    if serializer.is_valid():
        try:
            result = auth_service.login_user(
                serializer.validated_data['username'],
                serializer.validated_data['password']
            )
            return Response({
                'message': SUCCESS_LOGIN,
                'data': result
            })
            
        except BusinessException as e:
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    """
    User logout
    """
    try:
        auth_service.logout_user(request.user)
        return Response({'message': SUCCESS_LOGOUT})
    except BusinessException as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    """
    Get current user profile
    """
    try:
        profile_data = user_profile_service.get_user_profile(request.user.id)
        serializer = UserProfileSerializer(profile_data)
        return Response(serializer.data)
    except BusinessException as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_brand_profile(request):
    """
    Get current user's brand profile (if brand manager)
    """
    try:
        brand_data = brand_profile_service.get_brand_profile(request.user.id)
        serializer = BrandProfileSerializer(brand_data)
        return Response(serializer.data)
    except BusinessException as e:
        return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_brand_story(request):
    """
    Update brand sustainability story
    """
    serializer = BrandStoryUpdateSerializer(data=request.data)
    
    if serializer.is_valid():
        try:
            brand_profile = brand_profile_service.update_brand_story(
                request.user.id, 
                serializer.validated_data['sustainability_story']
            )
            return Response({
                'message': SUCCESS_BRAND_STORY_UPDATED,
                'data': BrandProfileSerializer(brand_profile).data
            })
            
        except BusinessException as e:
            return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_eco_points(request):
    """
    Add eco points and carbon saved to user profile
    """
    serializer = EcoPointsUpdateSerializer(data=request.data)
    
    if serializer.is_valid():
        try:
            result = user_profile_service.update_eco_points(
                request.user.id, 
                serializer.validated_data['points'],
                serializer.validated_data.get('carbon_saved', 0.0)
            )
            return Response({
                'message': SUCCESS_ECO_POINTS_ADDED,
                'data': result
            })
            
        except BusinessException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    """
    Update user profile information
    """
    try:
        # Get current profile data
        profile_data = user_profile_service.get_user_profile(request.user.id)
        serializer = UserProfileSerializer(profile_data, data=request.data, partial=True)
        
        if serializer.is_valid():
            # Update user basic info
            user = request.user
            if 'first_name' in request.data:
                user.first_name = request.data['first_name']
            if 'last_name' in request.data:
                user.last_name = request.data['last_name']
            user.save()
            
            # Update profile
            serializer.save()
            
            return Response({
                'message': SUCCESS_PROFILE_UPDATED,
                'data': serializer.data
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except BusinessException as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)