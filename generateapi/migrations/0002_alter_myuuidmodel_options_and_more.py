# Generated by Django 4.0.1 on 2022-01-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generateapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuuidmodel',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='myuuidmodel',
            old_name='present_dt',
            new_name='id',
        ),
        migrations.AddField(
            model_name='myuuidmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='myuuidmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
