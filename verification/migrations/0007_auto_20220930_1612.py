# Generated by Django 3.2.6 on 2022-09-30 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0006_auto_20220927_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonemodel',
            name='city',
            field=models.CharField(blank=True, default='0.0.0.0', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='ip_address',
            field=models.CharField(default='0.0.0.0', max_length=30),
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='lat_lng',
            field=models.CharField(blank=True, default='0.0.0.0', max_length=30, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='phonemodel',
            unique_together={('mobile', 'ip_address')},
        ),
    ]