# Generated by Django 3.0.4 on 2020-05-17 13:17

import datetime
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200517_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 17, 47, 31, 699368)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='article_persian_date',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2020, 5, 17, 17, 47, 31, 699368)),
        ),
    ]
