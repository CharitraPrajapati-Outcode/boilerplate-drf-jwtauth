from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.user.api.v1.views import UsersViewSet


app_name = 'user'

router = DefaultRouter()
router.register('', UsersViewSet, basename="users")

urlpatterns = [] + router.urls
