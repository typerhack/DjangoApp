# Generated by Django 3.0.4 on 2020-04-12 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200412_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 22, 2, 52, 1931)),
        ),
    ]