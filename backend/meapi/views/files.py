from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from fileroomg.models import FileItem

from ..serializers.files import FileItemListSerializer


class PrivateMeFileItemList(ListCreateAPIView):
    serializer_class = FileItemListSerializer
    queryset = FileItem.objects.all()


class PrivateMeFileItemDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = FileItemListSerializer
    queryset = FileItem.objects.all()
    lookup_field = "pk"
