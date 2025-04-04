from django.contrib import admin

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'age', 'can_be_contacted', 'can_data_be_shared']
    search_fields = ['username', 'email']
    list_filter = ['can_be_contacted', 'can_data_be_shared']