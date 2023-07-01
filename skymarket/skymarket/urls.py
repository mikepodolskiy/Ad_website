from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

# TODO здесь необходимо подключить нужные нам urls к проекту

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),

    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path("api/schema/swagger-ui/", SpectacularRedocView.as_view(url_name='api-schema'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
