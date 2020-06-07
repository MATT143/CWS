# Generated by Django 2.2.11 on 2020-05-29 20:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('custws', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertaskdetails',
            name='taskRevenue',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='usertaskdetails',
            name='creationTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 29, 20, 13, 18, 901119, tzinfo=utc)),
        ),
    ]