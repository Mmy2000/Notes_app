# Generated by Django 4.2.5 on 2023-10-05 02:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_alter_newslitter_created_at_alter_profile_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslitter',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 5, 2, 1, 37, 507010, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 5, 5, 1, 37, 505202)),
        ),
    ]
