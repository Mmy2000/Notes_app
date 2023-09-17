# Generated by Django 4.2.5 on 2023-09-17 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_profile_join_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 9, 17, 18, 53, 50, 489928, tzinfo=datetime.timezone.utc))),
            ],
            options={
                'verbose_name': 'NewsLitter',
                'verbose_name_plural': 'NewsLitter',
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 21, 53, 50, 488927)),
        ),
    ]
