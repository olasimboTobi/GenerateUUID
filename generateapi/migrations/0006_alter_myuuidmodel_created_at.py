# Generated by Django 4.0.1 on 2022-01-16 21:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('generateapi', '0005_alter_myuuidmodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuuidmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 16, 21, 3, 44, 472900, tzinfo=utc), null=True),
        ),
    ]
