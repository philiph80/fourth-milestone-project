# Generated by Django 3.1 on 2020-09-18 15:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_auto_20200918_1501'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAddress',
            new_name='UserProfile',
        ),
    ]