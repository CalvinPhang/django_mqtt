# Generated by Django 4.1.7 on 2023-03-20 14:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("uts_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sensorlog",
            name="time",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]