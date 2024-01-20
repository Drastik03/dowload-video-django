from django.db import models
from django.contrib.auth.models import User

class VideoModel(models.Model):
    title = models.CharField(max_length=200)
    videoLink = models.CharField(max_length=1000)
    download_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Titulo del video: ' + self.title + '\nUrl proporcionada: ' + self.videoLink + ' User: ' + self.user.username

