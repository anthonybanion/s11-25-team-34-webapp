"""
Admin configuration for User Profile and Brand Profile
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, BrandProfile

# Admin classes
class UserProfileInline(admin.StackedInline):
    """Inline editor for UserProfile in User admin"""
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'

# Custom User admin to include UserProfile
class CustomUserAdmin(UserAdmin):
    """Custom User admin that includes UserProfile"""
    inlines = (UserProfileInline,)

# Admin for UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    """Admin configuration for UserProfile"""
    list_display = ['user', 'phone', 'eco_points', 'total_carbon_saved', 'is_brand_manager']
    list_filter = ['is_brand_manager', 'eco_points']
    search_fields = ['user__username', 'user__email', 'phone']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')

# Admin for BrandProfile
class BrandProfileAdmin(admin.ModelAdmin):
    """Admin configuration for BrandProfile"""
    list_display = ['brand_name', 'user_profile', 'get_manager_email']
    list_filter = ['brand_name']
    search_fields = ['brand_name', 'user_profile__user__username', 'user_profile__user__email']
    
    def get_manager_email(self, obj):
        return obj.user_profile.user.email
    get_manager_email.short_description = 'Manager Email'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user_profile__user')

# Register models with admin
admin.site.unregister(User)                          # Unregister default User admin
admin.site.register(User, CustomUserAdmin)           # Register with custom admin
admin.site.register(UserProfile, UserProfileAdmin)   # Register UserProfile admin
admin.site.register(BrandProfile, BrandProfileAdmin) # Register BrandProfile admin