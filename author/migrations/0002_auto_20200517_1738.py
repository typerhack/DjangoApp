# Generated by Django 3.0.4 on 2020-05-17 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 17, 38, 20, 38725)),
        ),
    ]