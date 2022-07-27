from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .controllers.user import UserViewSet
from .controllers.user import UserViewSet
router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
