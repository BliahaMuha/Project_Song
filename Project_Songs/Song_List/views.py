from rest_framework import generics
from rest_framework.generics import get_object_or_404, ListAPIView

from .models import Artist, Album, Song
from rest_framework import viewsets
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer


# class ArtistList(generics.ListAPIView):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer
#
#
# class AlbumList(generics.ListAPIView):
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer
#
#
# class SongList(generics.ListAPIView):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumListByArtistAPIView(ListAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        artist_id = self.kwargs['id']
        return Album.objects.filter(artist=artist_id)


class ArtistListByArtistAPIView(generics.ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        artist_id = self.kwargs['id']
        return Artist.objects.filter(id=artist_id)


class SongListByArtistAPIView(generics.ListAPIView):
    serializer_class = SongSerializer

    def get_queryset(self):
        artist_id = self.kwargs['id']
        return Song.objects.filter(artist_id=artist_id)