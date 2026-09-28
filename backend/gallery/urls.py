from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin-1d067ead-9a85-41fa-9481-6e953c00c44e", admin.site.urls),
    path("api/v1/accounts", include("accountg.urls")),
    path("api/v1/me", include("meapi.urls")),
    path("api/v1/public", include("publicapi.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
