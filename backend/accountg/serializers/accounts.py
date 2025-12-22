from rest_framework.serializers import CharField, Serializer, ValidationError

from common.helpers.tokens import get_access_token

from ..models import User


class AccountLoginSerializer(Serializer):
    username = CharField(max_length=100, write_only=True)
    password = CharField(max_length=100, write_only=True)
    refresh = CharField(max_length=255, required=False, read_only=True)
    access = CharField(max_length=255, required=False, read_only=True)

    def validate(self, validated_data):
        user = User.objects.filter(username=validated_data.get("username"))
        if user.exists():
            if not user.first().check_password(validated_data.get("password")):
                raise ValidationError({"detail": "Invalid user!"})
        else:
            raise ValidationError({"detail": "Invalid user!"})
        validated_data["user"] = user.first()
        return super().validate(validated_data)

    def create(self, validated_data):
        validated_data["access"], validated_data["refresh"] = get_access_token(
            validated_data["user"]
        )
        return validated_data
