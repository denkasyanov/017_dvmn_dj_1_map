from collections import namedtuple

from django.db import models

Coordinates = namedtuple("Coordinates", "latitude longitude")


class Place(models.Model):
    title = models.CharField(max_length=250)
    description_short = models.CharField(max_length=1000)
    description_long = models.TextField()

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    @property
    def coordinates(self):
        return Coordinates(self.latitude, self.longitude)
