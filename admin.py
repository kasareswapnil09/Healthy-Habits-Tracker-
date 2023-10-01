# habits/admin.py

from django.contrib import admin
from .models import Habit

class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'frequency', 'goal')
    list_filter = ('frequency', 'user')  # Optional: Add filters for better admin interface
    search_fields = ('name', 'description')  # Optional: Add search functionality

# Register the Habit model with its admin class
admin.site.register(Habit, HabitAdmin)
