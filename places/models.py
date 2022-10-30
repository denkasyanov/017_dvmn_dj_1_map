from collections import namedtuple

from django.db import models

Coordinates = namedtuple("Coordinates", "latitude longitude")


class Place(models.Model):
    title = models.CharField(max_length=250)
    description_short = models.CharField(max_length=1000)
    description_long = models.TextField()

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.title

    @property
    def coordinates(self):
        return Coordinates(self.latitude, self.longitude)


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    position = models.PositiveSmallIntegerField()
    place = models.ForeignKey("Place", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.place.title} #{self.position}"
