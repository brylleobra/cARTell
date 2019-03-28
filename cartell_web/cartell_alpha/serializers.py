from rest_framework import serializers
from cartell_alpha.models import UserProfile

# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
