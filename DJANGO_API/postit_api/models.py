from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=150)

class Album(models.Model):
    name = models.CharField(max_length=150)
    band_id = models.ForeignKey(Band, on_delete=models.CASCADE)

class Song(models.Model):
    name = models.CharField(max_length=150)
    duration = models.FloatField(null=True, blank=True)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)

class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    score = models.DecimalField(max_digits=3, decimal_places=1)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='pictures', null=True)

    class Meta:
        ordering = ['-created']

class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.content

class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
