from ..serializers.user_serializer import UserSerializer
from ..models import CustomUser
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API TO GET ADD EDIT DELETE USERS.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
