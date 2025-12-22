from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from fileroomg.models import FileItem

from ..serializers.files import (
    PrivateMeFileItemListSerializer,
    PrivateMeFileItemDetailsSerializer,
)


class PrivateMeFileItemList(ListCreateAPIView):
    serializer_class = PrivateMeFileItemListSerializer
    get_queryset = lambda self: FileItem.objects.filter(user=self.request.user)


class PrivateMeFileItemDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateMeFileItemDetailsSerializer
    get_queryset = lambda self: FileItem.objects.filter(user=self.request.user)
    lookup_field = "uid"
