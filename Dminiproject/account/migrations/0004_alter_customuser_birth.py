# Generated by Django 4.2 on 2023-05-30 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_customuser_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 11, 28, 6, 173888, tzinfo=datetime.timezone.utc)),
        ),
    ]
