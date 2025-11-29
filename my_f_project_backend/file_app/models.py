from django.db import models

class FileItem(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="files/")

    def __str__(self):
        return f"ID:{self.id}, Title:{self.title}"
