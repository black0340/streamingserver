from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

def setName(instance,filename):
    return "me.jpg"

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name,max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
class Liveimg(models.Model):
    deviceUser = models.CharField(max_length=100, null=True)
    deviceId = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=setName,storage=OverwriteStorage())

# Create your models here.
