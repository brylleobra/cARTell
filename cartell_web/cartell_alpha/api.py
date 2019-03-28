from cartell_alpha.models import UserProfile
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

# User Viewset


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = UserSerializer
