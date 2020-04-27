# Generated by Django 3.0.4 on 2020-04-12 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200412_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='video_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 23, 33, 40, 21474)),
        ),
    ]