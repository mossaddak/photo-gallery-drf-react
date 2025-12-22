from django.urls import path

from ..views.accounts import AccountLoginView

urlpatterns = [
    path(r"/login", AccountLoginView.as_view(), name="accountg.login"),
]
