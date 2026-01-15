from rest_framework.serializers import CharField, Serializer, ValidationError

from common.helpers.tokens import get_access_token, get_id
from common.helpers.emails import send_email

from ..models import User


class AccountLoginSerializer(Serializer):
    username = CharField(max_length=100, write_only=True, required=False)
    password = CharField(max_length=100, write_only=True, required=False)
    login_otp = CharField(max_length=6, write_only=True, required=False)
    refresh = CharField(max_length=255, required=False, read_only=True)
    access = CharField(max_length=255, required=False, read_only=True)

    def validate(self, validated_data):
        filters = {}
        login_otp = validated_data.get("login_otp", None)
        username = validated_data.get("username")

        if login_otp:
            filters["login_otp"] = login_otp
        elif username:
            filters["username"] = username

        user = User.objects.filter(**filters)

        if user.exists() and not login_otp:
            if not user.first().check_password(validated_data.get("password")):
                raise ValidationError({"detail": "Invalid user!"})
        elif user.exists() and not username:
            pass
        else:
            raise ValidationError({"detail": "Invalid user!"})

        validated_data["user"] = user.first()
        return super().validate(validated_data)

    def create(self, validated_data):
        user = validated_data["user"]
        if validated_data.get("username") and not validated_data.get("login_otp"):
            user.login_otp = get_id(User, "login_otp")
            user.save_dirty_fields()
            send_email(user, "emails/login_otp.html", {"subject": "Your Login OTP", "otp": user.login_otp})
        else:
            validated_data["access"], validated_data["refresh"] = get_access_token(
                user
            )
            user.login_otp = None
            user.save_dirty_fields()
        return validated_data
