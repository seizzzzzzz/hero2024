# Generated by Django 5.1.2 on 2024-10-27 16:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_calendar_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='calendar_data',
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('fasting_sugar', models.CharField(blank=True, max_length=50, null=True)),
                ('breakfast', models.CharField(blank=True, max_length=50, null=True)),
                ('lunch', models.CharField(blank=True, max_length=50, null=True)),
                ('dinner', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]