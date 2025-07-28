from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.user.models import User
from apps.user.api.v1.serializers import UserSerializer

# Create your views here.
class UsersViewSet(ModelViewSet):
    """ViewSet for managing users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
