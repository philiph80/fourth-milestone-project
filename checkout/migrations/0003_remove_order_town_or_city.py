# Generated by Django 3.1 on 2020-08-31 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200830_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='town_or_city',
        ),
    ]
