"""
v1 view for swagger
"""
from decouple import config
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from config.urls import urlpatterns

swagger_info = openapi.Info(
    title="Boilerplate API docs",
    default_version='v1',
    description="APIs of Boilerplate platform",
)

drf_yasg_swagger_view = get_schema_view(
    swagger_info,
    patterns=urlpatterns,
    url=config('API_URL'),
    public=True,
    permission_classes=[permissions.AllowAny],
)
