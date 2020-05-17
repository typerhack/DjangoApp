from django.db import models
from datetime import datetime
from django_jalali.db import models as jmodels
import jdatetime
import persian


# Create your models here.
class Banner(models.Model):
    project_name = models.CharField(max_length=100)
    project_location = models.CharField(max_length=100)
    project_alt = models.CharField(max_length=100)
    project_photo = models.ImageField(upload_to='photo_banner/%Y/%m/%d/')
    add_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    # To use "jdatetime.datetime.now" a minor change has been done in setting: "USE_TZ = False"
    # i added a different time field instead.
    banner_add_date = jmodels.jDateField(default=jdatetime.datetime.now)
    time_added = models.TimeField(default=datetime.now)

    def banner_persian_date_report(self):
        date = self.banner_add_date.strftime('%Y/%m/%d')
        time = self.time_added.strftime('%H:%M')
        time_and_date = persian.convert_en_numbers(f"تاریخ: {date} - ساعت: {time}")
        return time_and_date

    def __str__(self):
        return self.project_name
