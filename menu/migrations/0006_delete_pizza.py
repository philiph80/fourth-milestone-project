# Generated by Django 3.1 on 2020-09-07 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20200907_1423'),
        ('checkout', '0006_auto_20200907_1423'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pizza',
        ),
    ]
