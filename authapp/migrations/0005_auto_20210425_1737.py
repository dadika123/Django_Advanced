# Generated by Django 2.2 on 2021-04-25 17:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20210422_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 17, 37, 40, 359529, tzinfo=utc)),
        ),
    ]
