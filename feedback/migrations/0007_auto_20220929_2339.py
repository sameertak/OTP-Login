# Generated by Django 3.2.6 on 2022-09-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0006_alter_responsemodel_res3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsemodel',
            name='res1',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='responsemodel',
            name='res2',
            field=models.CharField(max_length=25),
        ),
    ]
