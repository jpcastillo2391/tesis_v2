from django.db import models

# Create your models here.   voy  a buscar como implementar users y passwordsaqui
class user(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def get_absolute_url (self):
        return reversed('musicss:detalles', kwards={'pk':self.pk})
    def __str__(self):
        return self.album_title + ' - ' + self.artist
