"""
Views for the User
"""
from rest_framework import generics, authentication, permissions
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
    OpenApiExample,
)
from drf_spectacular.types import OpenApiTypes
from user.serializers import UserSerializer, AuthTokenSerializer

from django.shortcuts import render


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """
    View to Create a new user in the System
    """

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """
    View to Generate Auth token for identification for the users requests
    """

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


@extend_schema_view(
    get=extend_schema(
        description="Returns user's details if the user is authenticated."
    ),
    patch=extend_schema(
        description="Edits user's details and returns the modified details. Only a single property from the users details can be modified",
    ),
    put=extend_schema(
        description="Edits user's details and returns the modified details"
    ),
)
class ManageUserView(generics.RetrieveUpdateAPIView):
    """
    Manage the authenticated user
    """

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Retrieve and return the authenticated user
        """
        return self.request.user
