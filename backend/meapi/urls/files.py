from django.urls import path

from ..views.files import PrivateMeFileItemList, PrivateMeFileItemDetails

urlpatterns = [
    path(
        r"/<int:pk>", PrivateMeFileItemDetails.as_view(), name="meapi-file-item-details"
    ),
    path(r"", PrivateMeFileItemList.as_view(), name="meapi-file-item-list"),
]
