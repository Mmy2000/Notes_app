# Generated by Django 4.2.5 on 2023-09-14 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_profile_first_name_remove_profile_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='headline',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 14, 9, 37, 16, 710297)),
        ),
    ]
