from django.db import models

from django.contrib.auth.models import User

# Create your models here.

genre_choices = (('Rock','Rock'),('Pop','Pop'),('Country','Country'),('Jazz','Jazz'),('Blues','Blues'))

class Album(models.Model):
    album_name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    user = models.ForeignKey(User,related_name='artist_user',on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.album_name}_{self.artist}"

class Track(models.Model):
    album = models.ForeignKey(Album,related_name="album_track",on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    duration = models.FloatField()
    genre = models.CharField(max_length=30,choices=genre_choices)

    class Meta:
        unique_together = ['album','title']
        ordering = ['genre']

    def __str__(self):
        return f"{self.id}_{self.title}"
