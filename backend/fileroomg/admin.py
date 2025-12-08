from django.contrib import admin
from .models import FileItem

class FileItemAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "file"]

admin.site.register(FileItem, FileItemAdmin)
