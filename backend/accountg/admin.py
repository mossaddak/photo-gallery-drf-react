from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["uid", "slug", "title", "avatar"]

admin.site.register(User, UserAdmin)