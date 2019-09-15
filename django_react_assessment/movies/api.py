from rest_framework import viewsets, permissions
from .serializers import *


class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = MovieSerializer

    queryset = Movie.objects.all()
