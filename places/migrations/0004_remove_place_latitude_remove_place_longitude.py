# Generated by Django 4.1.4 on 2022-12-21 14:54
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0003_place_location"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="place",
            name="latitude",
        ),
        migrations.RemoveField(
            model_name="place",
            name="longitude",
        ),
    ]