# Generated by Django 2.2.6 on 2019-10-30 12:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mystorage', '0003_file'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='File',
            new_name='Files',
        ),
    ]
