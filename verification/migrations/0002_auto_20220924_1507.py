# Generated by Django 3.2.6 on 2022-09-24 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 15, 7, 25, 706490)),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
