from rest_framework.serializers import ModelSerializer

from fileroomg.models import FileItem, FileItemConnector


class FileItemListSerializer(ModelSerializer):

    class Meta:
        model = FileItem
        fields = ["id", "title", "file", "description"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user

        file_item = FileItem.objects.create(**validated_data)
        FileItemConnector.objects.create(file_item=file_item, user=user)
        return validated_data
