# Generated by Django 4.1.5 on 2023-02-03 21:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='bookingNumber',
            field=models.CharField(default=datetime.datetime(2023, 2, 3, 21, 59, 57, 882150, tzinfo=datetime.timezone.utc), max_length=255),
        ),
    ]
