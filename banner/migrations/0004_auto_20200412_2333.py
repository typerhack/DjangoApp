# Generated by Django 3.0.4 on 2020-04-12 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0003_auto_20200412_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 23, 33, 40, 22473)),
        ),
    ]