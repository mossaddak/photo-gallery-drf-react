from django.urls import path, include

urlpatterns = [
    path(r"/files", include("meapi.urls.files")),
]
