from django.db import models
from datetime import datetime

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos_author/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    start_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.first_name} {self.last_name}"