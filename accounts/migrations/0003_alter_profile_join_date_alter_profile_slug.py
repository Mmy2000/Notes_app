# Generated by Django 4.2.5 on 2023-09-14 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_bio_profile_first_name_profile_join_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 14, 8, 16, 19, 636850)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]