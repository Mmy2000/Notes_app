# Generated by Django 4.2.5 on 2023-09-14 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_profile_slug_alter_profile_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 14, 12, 24, 32, 534320)),
        ),
    ]
