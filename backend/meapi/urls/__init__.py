from django.urls import path, include

from ..views.me import PrivateMeDetails

urlpatterns = [
    path(r"", PrivateMeDetails.as_view()),
    path(r"/files", include("meapi.urls.files")),
]
