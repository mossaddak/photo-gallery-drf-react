from rest_framework.generics import RetrieveUpdateAPIView

from meapi.serializers.me import PrivateMeDetailsSerializer, PrivateMeHeaderSerializer


class PrivateMeDetails(RetrieveUpdateAPIView):
    serializer_class = PrivateMeDetailsSerializer

    def get_serializer_class(self):
        if self.request.query_params.get("is_header") == "true":
            return PrivateMeHeaderSerializer
        return super().get_serializer_class()

    def get_object(self):
        return self.request.user
