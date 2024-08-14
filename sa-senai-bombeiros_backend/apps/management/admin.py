from django.contrib.gis import admin
from django.contrib.auth.hashers import make_password
from apps.management.models import (
    User,
    Admin,
    Firefighter,
)


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active", "is_superuser"]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form

    def get_fieldsets(self, request, obj=None):
        if obj:
            return [(None, {"fields": ("name", "email", "is_active")})]
        return [
            (None, {"fields": ("name", "email", "password", "is_active")})
        ]

    def save_model(self, request, obj, form, change):
        if "password" in form.changed_data:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)


class AdminAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "cpf", "phone"]
    search_fields = ["user"]
    readonly_fields = ["updated_at", "created_at"]


admin.site.register(Admin, AdminAdmin)


class FirefighterAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "cpf", "phone"]
    search_fields = ["user"]
    readonly_fields = ["updated_at", "created_at"]


admin.site.register(Firefighter, FirefighterAdmin)
