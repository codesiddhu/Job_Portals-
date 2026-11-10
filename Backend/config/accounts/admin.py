from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = ('id','username','email','role','is_active','is_staff',)

    list_filter = ('role','is_active','is_staff',)
    search_fields = ('username','email',)
    fieldsets = UserAdmin.fieldsets + (('Additional Information', {'fields': ('role','phone','profile_image','bio','location',)}),)
