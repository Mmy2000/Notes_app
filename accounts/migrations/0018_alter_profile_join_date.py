# Generated by Django 4.2.5 on 2023-09-17 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_profile_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 21, 15, 40, 988512)),
        ),
    ]