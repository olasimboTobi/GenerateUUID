# Generated by Django 4.0.1 on 2022-01-16 20:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generateapi', '0003_remove_myuuidmodel_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuuidmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]