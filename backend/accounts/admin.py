from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'role', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Extra', {'fields': ('role', 'phone', 'date_of_birth')}),
    )
