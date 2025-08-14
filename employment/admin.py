from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Employee

class CustomUserAdmin(UserAdmin):
    # Fields to display in the admin list
    list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    # Field layout when editing/adding a user
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "phone", "company_name", "employee_count", "full_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
    )

    # Fields for "Add user" form in admin
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)  # ✅ changed from 'username' to 'email'

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "department", "position", "start_date")
    search_fields = ("first_name", "last_name", "email")
