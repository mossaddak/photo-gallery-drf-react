from django.contrib import admin
from django.urls import path

from .views import FileItemView

urlpatterns = [
    path(r"", FileItemView.as_view(), name="file-item-list"),
]
