# Generated by Django 5.1.3 on 2025-01-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_description_event_show_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='banned',
            field=models.BooleanField(default=False),
        ),
    ]
