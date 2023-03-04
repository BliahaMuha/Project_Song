from django.contrib import admin
from .models import Album, Artist, Song


# Register your models here.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'artist')
    list_filter = ('title', 'year', 'artist')
    list_editable = ('title', 'year', 'artist')
    list_display_links = None


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    list_editable = ('name',)
    list_display_links = None


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('song', 'track_number',)
    list_filter = ('song', 'track_number',)
    list_editable = ('song', 'track_number',)
    list_display_links = None