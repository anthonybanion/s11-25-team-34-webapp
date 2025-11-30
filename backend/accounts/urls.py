"""
User Profile and Brand Profile URLs

File: urls.py
Author: Anthony Bañon
Created: 2025-11-29
Last Updated: 2025-11-29
"""

from django.urls import path
from . import views

urlpatterns = [
    # Authentication endpoints
    path('auth/register/', views.register_user, name='register-user'),
    path('auth/register/brand-manager/', views.register_brand_manager, name='register-brand-manager'),
    path('auth/login/', views.login_user, name='login-user'),
    path('auth/logout/', views.logout_user, name='logout-user'),
    
    # User profile endpoints
    path('profile/', views.get_user_profile, name='get-user-profile'),
    path('profile/update/', views.update_user_profile, name='update-user-profile'),
    path('profile/eco-points/', views.add_eco_points, name='add-eco-points'),
    
    # Brand profile endpoints (for brand managers)
    path('brand/profile/', views.get_brand_profile, name='get-brand-profile'),
    path('brand/story/', views.update_brand_story, name='update-brand-story'),
]