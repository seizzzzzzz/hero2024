# Generated by Django 5.1.2 on 2024-10-27 15:57

import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='calendar_data',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
