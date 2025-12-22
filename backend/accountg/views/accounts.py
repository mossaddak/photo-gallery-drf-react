from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from ..serializers.accounts import AccountLoginSerializer

class AccountLoginView(CreateAPIView):
    serializer_class = AccountLoginSerializer
    permission_classes = [AllowAny]
