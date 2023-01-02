# Generated by Django 4.1.4 on 2023-01-02 01:45
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0011_alter_place_description_short"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="place",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="places.place",
            ),
        ),
    ]