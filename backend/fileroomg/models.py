from django.db import models

from common.helpers.media_paths import get_media_path_prefix

from common.models import BaseModel


class FileItem(BaseModel):
    file = models.FileField(upload_to=get_media_path_prefix)
    user = models.ForeignKey(
        "accountg.User", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"ID:{self.id}, Title:{self.title}"


class FileItemConnector(BaseModel):
    file_item = models.ForeignKey(FileItem, on_delete=models.CASCADE)
    user = models.ForeignKey("accountg.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"ID:{self.file_item.id}, User ID:{self.user.id}"
