from django.db import models

from django.contrib.auth.models import User
NULLABLE = {'null': True, 'blank': True}


class Film(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    description = models.TextField(verbose_name='description')
    release_date = models.IntegerField(verbose_name='release date', **NULLABLE)
    logo = models.ImageField(verbose_name='logo', **NULLABLE)

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'film')

