from rest_framework.serializers import ModelSerializer

from fileroomg.models import FileItem, FileItemConnector


class PublicFileItemListSerializer(ModelSerializer):

    class Meta:
        model = FileItem
        fields = ["uid", "title", "file", "description", "created_at", "updated_at"]


class PublicFileItemDetailsSerializer(ModelSerializer):

    class Meta:
        model = FileItem
        fields = ["uid", "title", "file", "description", "created_at", "updated_at"]
