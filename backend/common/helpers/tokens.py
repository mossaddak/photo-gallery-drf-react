import random

from rest_framework_simplejwt.tokens import RefreshToken


def get_access_token(user: object) -> tuple:
    """Generate a unique access token for a user."""

    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token), str(refresh)


def get_id(
    model_name: str,
    field_name: str,
    special_character: str = "",
    label: str = "",
    length: int = 6,
) -> str:
    """Generate a unique ID for a given model"""

    start = 10 ** (length - 1)
    end = (10**length) - 1
    id = random.randint(start, end)
    if model_name.objects.filter(**{field_name: id}).exists():
        return get_id(model_name, field_name, special_character, label, length)
    return f"{special_character}{label}{str(id)}"
