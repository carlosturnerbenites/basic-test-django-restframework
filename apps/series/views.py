from .models import Genre, Serie
from rest_framework import viewsets
from .serializers import GenreSerializer, SerieSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Genre.objects.all() #.order_by('-date_joined')
    serializer_class = GenreSerializer


class SerieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
