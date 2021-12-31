from django.db import models
from django.contrib.auth.models import User
from songs.models import Song
        
from django.conf.global_settings import DATETIME_INPUT_FORMATS



# Create your models here.
class Preference(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField()
    songs = models.ManyToManyField(Song,related_name='songs')
    some_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username}--{self.active}"
