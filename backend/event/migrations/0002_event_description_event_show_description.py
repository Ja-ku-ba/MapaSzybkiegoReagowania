# Generated by Django 5.1.3 on 2025-01-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(default=1, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='show_description',
            field=models.BooleanField(default=False),
        ),
    ]
