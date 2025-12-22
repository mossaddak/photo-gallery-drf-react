from rest_framework.serializers import ModelSerializer

from accountg.models import User


class PrivateMeHeaderSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uid",
            "username",
            "first_name",
            "last_name",
            "avatar",
            "created_at",
            "updated_at",
        ]


class PrivateMeDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uid",
            "username",
            "email",
            "status",
            "first_name",
            "last_name",
            "avatar",
            "is_active",
            "date_joined",
            "last_login",
            "created_at",
            "updated_at",
        ]
