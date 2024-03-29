# Generated by Django 4.1.5 on 2023-02-05 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_reservation_bookingnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='isCheckedIn',
            field=models.CharField(default='false', max_length=255),
        ),
        migrations.AddField(
            model_name='reservation',
            name='isCheckedOut',
            field=models.CharField(default='false', max_length=255),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='bookingNumber',
            field=models.CharField(default=datetime.datetime(2023, 2, 5, 13, 33, 51, 791131, tzinfo=datetime.timezone.utc), max_length=255),
        ),
    ]
