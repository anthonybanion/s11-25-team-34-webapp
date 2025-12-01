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
    path('auth/register/', views.RegisterUserView.as_view(), name='register-user'),
    path('auth/register/brand-manager/', views.RegisterBrandManagerView.as_view(), name='register-brand-manager'),
    path('auth/login/', views.LoginUserView.as_view(), name='login-user'),
    path('auth/logout/', views.LogoutUserView.as_view(), name='logout-user'),
    path('auth/change-password/', views.ChangePasswordView.as_view(), name='change-password'),

    
    # User profile endpoints
    path('profile/', views.GetUserProfileView.as_view(), name='get-user-profile'),
    path('profile/update/', views.UpdateUserProfileView.as_view(), name='update-user-profile'),
    path('profile/eco-points/', views.AddEcoPointsView.as_view(), name='add-eco-points'),
    path('profile/delete/', views.DeleteUserAccountView.as_view(), name='delete-user-account'),
    
    # Brand profile endpoints
    path('brand/profile/', views.GetBrandProfileView.as_view(), name='get-brand-profile'),
    path('brand/story/', views.UpdateBrandStoryView.as_view(), name='update-brand-story'),
    path('brand/delete/', views.DeleteBrandProfileView.as_view(), name='delete-brand-profile'),
]