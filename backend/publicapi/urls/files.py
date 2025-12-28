from django.urls import path

from ..views.files import PublicFileItemList, PublicFileItemDetails

urlpatterns = [
    path(
        r"<uuid:uid>", PublicFileItemDetails.as_view(), name="publicapi.file-item-details"
    ),
    path(r"", PublicFileItemList.as_view(), name="publicapi.file-item-list"),
]
