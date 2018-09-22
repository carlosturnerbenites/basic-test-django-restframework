from .models import Genre, Serie
from rest_framework import serializers


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('url', 'name')


class SerieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serie
        fields = ('url', 'name', 'rate', 'airing_at', 'genres')
