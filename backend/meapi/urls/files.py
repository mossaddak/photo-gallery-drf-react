from django.urls import path

from ..views.files import PrivateMeFileItemList, PrivateMeFileItemDetails

urlpatterns = [
    path(
        r"/<uuid:uid>", PrivateMeFileItemDetails.as_view(), name="meapi-file-item-details"
    ),
    path(r"", PrivateMeFileItemList.as_view(), name="meapi-file-item-list"),
]
