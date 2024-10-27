# Generated by Django 5.1.2 on 2024-10-27 16:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_user_calendar_data_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10)),
                ('fasting_sugar', models.CharField(blank=True, max_length=100, null=True)),
                ('breakfast', models.CharField(blank=True, max_length=100, null=True)),
                ('lunch', models.CharField(blank=True, max_length=100, null=True)),
                ('dinner', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]