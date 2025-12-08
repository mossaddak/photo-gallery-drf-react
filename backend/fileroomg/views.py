from rest_framework.generics import ListCreateAPIView

from .models import FileItem
from .searializers import FileItemListSerializer


class FileItemView(ListCreateAPIView):
    serializer_class = FileItemListSerializer
    queryset = FileItem.objects.all()
