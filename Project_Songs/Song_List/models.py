from django.db import models


# Create your models here.
class Artist(models.Model):
    """
    Модель Исполнитель
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, default=name)

    def __str__(self):
        return self.name


class Album(models.Model):
    """
    Модель Альбом
    """
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    slug = models.SlugField(max_length=100, default='title')

    def __str__(self):
        return self.title


class Song(models.Model):
    """
    Модель Песня
    """
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    song = models.CharField(max_length=100)
    track_number = models.IntegerField()
    slug = models.SlugField(max_length=100, default='song')

    def __str__(self):
        return self.song
