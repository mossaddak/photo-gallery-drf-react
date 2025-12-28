from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from fileroomg.models import FileItem

from ..serializers.files import (
    PublicFileItemListSerializer,
    PublicFileItemDetailsSerializer,
)


class PublicFileItemList(ListAPIView):
    serializer_class = PublicFileItemListSerializer
    permission_classes = [AllowAny]
    queryset = FileItem.objects.all()


class PublicFileItemDetails(RetrieveAPIView):
    serializer_class = PublicFileItemDetailsSerializer
    permission_classes = [AllowAny]
    queryset = FileItem.objects.all()
    lookup_field = "uid"
