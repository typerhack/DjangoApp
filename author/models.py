from django.db import models
from datetime import datetime
from django_jalali.db import models as jmodels
import persian


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos_author/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    start_date = models.DateTimeField(default=datetime.now())
    start_persian_date = jmodels.jDateTimeField(default=datetime.now())

    def persian_date_report(self):
        time_and_date = persian.convert_en_numbers(self.start_persian_date.strftime('تاریخ: %Y/%m/%d - ساعت: %H:%M'))
        return time_and_date

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
