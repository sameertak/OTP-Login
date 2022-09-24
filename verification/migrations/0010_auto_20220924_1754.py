# Generated by Django 3.2.6 on 2022-09-24 12:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0009_auto_20220924_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='city',
            field=models.CharField(default='NaN', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 12, 24, 3, 311471, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='lat_lng',
            field=models.CharField(default='NaN', max_length=10, null=True),
        ),
    ]
