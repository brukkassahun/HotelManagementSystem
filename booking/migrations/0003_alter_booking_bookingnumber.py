# Generated by Django 4.1.5 on 2023-01-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_members_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bookingNumber',
            field=models.CharField(max_length=255),
        ),
    ]
