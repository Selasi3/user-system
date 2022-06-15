from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FileUpload(models.Model):
    file_name = models.CharField(max_length=200)
    file = models.FileField(upload_to="media")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file_name