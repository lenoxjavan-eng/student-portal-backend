from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('student', 'program', 'status', 'submitted_at')
    list_filter = ('status',)
