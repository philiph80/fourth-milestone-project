# Generated by Django 3.1 on 2020-09-15 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='collection',
        ),
    ]
