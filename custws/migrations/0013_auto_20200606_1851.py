# Generated by Django 2.2.11 on 2020-06-06 13:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('custws', '0012_auto_20200605_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
        migrations.AlterField(
            model_name='usertaskdetails',
            name='creationTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 6, 13, 21, 26, 394878, tzinfo=utc)),
        ),
    ]
