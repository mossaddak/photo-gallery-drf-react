from rest_framework.exceptions import APIException

from rest_framework.views import exception_handler


class ValidationError(APIException):
    status_code = 400
    default_detail = "Invalid request"
    default_code = "invalid"

    def __init__(self, detail=None):
        if detail is None:
            detail = self.default_detail
        self.detail = {"detail": str(detail)}


def custom_exception_handler(exc, context):
    """
    Convert all validation errors so that:
    - Field keys remain
    - All messages for a field are combined into a single string
    """
    response = exception_handler(exc, context)

    if response is not None:
        new_data = {}
        for key, value in response.data.items():
            if isinstance(value, list):
                new_data[key] = ", ".join(str(msg) for msg in value)
            elif isinstance(value, dict):
                nested_messages = []
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, list):
                        nested_messages.append(
                            f"{sub_key}: {', '.join(str(m) for m in sub_value)}"
                        )
                    else:
                        nested_messages.append(f"{sub_key}: {sub_value}")
                new_data[key] = " | ".join(nested_messages)
            else:
                new_data[key] = str(value)

        response.data = new_data

    return response
