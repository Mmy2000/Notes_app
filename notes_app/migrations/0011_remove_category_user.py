# Generated by Django 4.2.5 on 2023-09-17 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0010_category_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
    ]