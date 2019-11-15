from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class UserAdminCustom(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff',)
    # Displayed when updating
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'middle_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    # Displayed when creating a new user
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email', 'first_name', 'middle_name', 'last_name', 'password1',
                    'password2'
                )
            }
        ),
    )
    search_fields = ('email', 'first_name', 'middle_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name')
    filter_horizontal = ()

admin.site.register(User, UserAdminCustom)
