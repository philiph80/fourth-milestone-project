# Generated by Django 3.1 on 2020-09-07 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20200826_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('PIZZA', 'Pizza'), ('SIDE', 'Side'), ('DESSERT', 'Dessert'), ('DRINK', 'Drink')], default='PIZZA', max_length=20)),
                ('small_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('regular_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('large_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('toppings', models.ManyToManyField(related_name='pizzas', through='menu.ToppingAmount', to='menu.Topping')),
            ],
        ),
        migrations.AlterField(
            model_name='toppingamount',
            name='pizza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topping_amounts', to='menu.product'),
        ),
    ]
