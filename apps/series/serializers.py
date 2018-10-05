from .models import Genre, Serie
from rest_framework import serializers


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'url', 'name')


class SerieSerializer(serializers.HyperlinkedModelSerializer):
    genres = GenreSerializer(many=True) # read_only=True

    class Meta:
        model = Serie
        fields = ('id', 'url', 'name', 'rate', 'airing_at', 'genres')

    def create(self, validated_data):
        genres_data = validated_data.pop('genres')
        serie = Serie.objects.create(**validated_data)
        for genres_data in genres_data:
            genre = Genre.objects.create(**genres_data)
            serie.genres.add(genre)
        return serie
    """
    def update(self, instance, validated_data):
    """
