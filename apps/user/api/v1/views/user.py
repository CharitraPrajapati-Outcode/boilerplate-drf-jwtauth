from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from apps.user.models import User
from apps.user.api.v1.serializers import UserSerializer, UpdateUserSerializer

# Create your views here.
class UsersViewSet(ModelViewSet):
    """ViewSet for managing users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = {
        'email': ['exact'],
        'name': ['exact'],
    }
    search_fields = ['name', 'email']

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return UpdateUserSerializer
        return UserSerializer
