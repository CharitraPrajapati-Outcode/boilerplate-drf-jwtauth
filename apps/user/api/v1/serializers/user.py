from rest_framework.serializers import ModelSerializer
from apps.user.models import User


class UserSerializer(ModelSerializer):
    """Serializer for User model."""
    
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True},
        }
