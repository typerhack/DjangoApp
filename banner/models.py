from django.db import models
from datetime import datetime

# Create your models here.
class Banner(models.Model):
    project_name = models.CharField(max_length=100)
    project_location = models.CharField(max_length=100)
    project_alt = models.CharField(max_length=100)
    project_photo = models.ImageField(upload_to='photo_banner/%Y/%m/%d/')
    add_date = models.DateTimeField(default=datetime.now())
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name