# Generated by Django 3.2.6 on 2022-09-24 12:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0008_auto_20220924_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonemodel',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='phonemodel',
            name='long',
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='lat_lng',
            field=models.CharField(default='NaN', max_length=10),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 12, 23, 5, 826177, tzinfo=utc)),
        ),
    ]
