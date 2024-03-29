from django.conf import settings
from django.conf.urls import include, static
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from apps.accounts.urls import router as accounts_router

MEDIA_ROOT = settings.MEDIA_ROOT
MEDIA_URL = settings.MEDIA_URL
STATIC_URL = settings.STATIC_URL

router = DefaultRouter()
router.registry.extend(accounts_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^api/v1/", include(router.urls)),
    re_path(r"^api/v1/", include("apps.accounts.urls", namespace="accounts")),
]

urlpatterns += static.static(MEDIA_URL, document_root=MEDIA_ROOT)
