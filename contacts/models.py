from django.db import models
from django_jalali.db import models as jmodels
import persian


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    contact_date = models.DateTimeField(auto_now_add=True)
    contact_date_persian = jmodels.jDateTimeField(auto_now_add=True)
    user_id = models.IntegerField(blank=True)

    def contact_date_report(self):
        date = self.contact_date_persian.strftime('%Y/%m/%d')
        time = self.contact_date.strftime('%H:%M')
        time_and_date = persian.convert_en_numbers(f"تاریخ: {date} - ساعت: {time}")
        return time_and_date

    def __str__(self):
        return self.subject
