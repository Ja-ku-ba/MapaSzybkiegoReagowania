from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "email",
        "username",
    )
    list_filter = (
        "email",
        "username",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": (
            "email", 
            "password",
            "username")}
        ),
        ("Permissions", {"fields": (
            "is_staff", 
            "is_active", 
            "groups", 
            "user_permissions")}
        ),
    )
    add_fieldsets = (
        ( None, {"fields": (
            "username",
            "email",
            "password1",
            "password2",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions")}
        ),
    )
    search_fields = ("email", "username")
    ordering = ("username",)