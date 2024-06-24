from django.shortcuts import render

from rest_framework.versioning import URLPathVersioning
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import GameSerializer, GenreSerializer

from shop.models import Game, Genre


class APIVersioning(URLPathVersioning):
    default_version = 1
    allowed_versions = 1
    version_param = 1


class GamesAPIList(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    versioning_class = APIVersioning
    permission_classes = (IsAuthenticatedOrReadOnly,)


class GamesAPIUpdate(RetrieveUpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated & IsAdminUser)


class GamesAPIDestroy(RetrieveDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated & IsAdminUser)


class GenresAPIList(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenresAPIDestroy(RetrieveDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated & IsAdminUser)


