# Generated by Django 4.1.5 on 2023-02-15 22:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=255)),
                ('bookingNumber', models.CharField(default=datetime.datetime(2023, 2, 15, 22, 34, 1, 785713, tzinfo=datetime.timezone.utc), max_length=255)),
                ('checkIn', models.DateField()),
                ('checkOut', models.DateField()),
                ('firstName', models.CharField(max_length=255)),
                ('middelName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('contactNumber', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('idCardType', models.CharField(max_length=255)),
                ('idCardNumber', models.CharField(max_length=255)),
                ('roomType', models.CharField(max_length=255)),
                ('roomNumber', models.CharField(max_length=255)),
                ('paymentStatus', models.CharField(max_length=255)),
                ('total', models.FloatField()),
                ('isCheckedIn', models.CharField(default='false', max_length=255)),
                ('isCheckedOut', models.CharField(default='false', max_length=255)),
            ],
        ),
    ]