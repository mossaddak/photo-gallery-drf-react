from django.urls import path, include

urlpatterns = [
    path("", include("accountg.urls.accounts")),
]
