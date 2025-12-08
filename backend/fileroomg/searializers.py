from rest_framework.serializers import ModelSerializer

from .models import FileItem


class FileItemListSerializer(ModelSerializer):

    class Meta:
        model = FileItem
        fields = ["id", "title", "file", "description"]
