from rest_framework import serializers

from .models import Artist, Album, Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'artist', 'year', )


class SongSerializer(serializers.ModelSerializer):
    album = serializers.StringRelatedField()

    class Meta:
        model = Song
        fields = '__all__'