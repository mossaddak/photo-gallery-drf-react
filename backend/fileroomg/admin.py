from django.contrib import admin

from .models import FileItem, FileItemConnector


class FileItemAdmin(admin.ModelAdmin):
    list_display = ["uid", "slug", "title", "file"]


class FileItemConnectorAdmin(admin.ModelAdmin):
    list_display = ["uid", "slug", "file_item", "user"]


admin.site.register(FileItem, FileItemAdmin)
admin.site.register(FileItemConnector, FileItemConnectorAdmin)
