# Generated by Django 4.1.4 on 2023-01-02 01:17
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0009_alter_place_description_long"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="place",
            name="place_id",
        ),
    ]
