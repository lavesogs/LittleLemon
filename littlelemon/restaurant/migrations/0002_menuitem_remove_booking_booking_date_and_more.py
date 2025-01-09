# Generated by Django 5.1.4 on 2025-01-09 18:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('inventory', models.SmallIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='no_of_guests',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='title',
        ),
        migrations.AddField(
            model_name='booking',
            name='first_name',
            field=models.CharField(default='Guest', max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation_slot',
            field=models.SmallIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_item_description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='menu',
            name='name',
            field=models.CharField(default='Menu Item', max_length=100),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(),
        ),
    ]