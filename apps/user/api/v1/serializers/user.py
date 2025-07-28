from rest_framework.serializers import ModelSerializer
from apps.user.models import User


class UserSerializer(ModelSerializer):
    """Serializer for User model."""
    
    class Meta:
        model = User
        fields = ["id", "email", "name", "password", "deleted_at"]
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True},
        }


class UpdateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name",]
        read_only_fields = ['id', 'email', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True},
        }
