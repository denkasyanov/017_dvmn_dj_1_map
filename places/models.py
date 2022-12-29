from django.contrib.gis.db.models import PointField
from django.db import models
from django.templatetags.static import static


class Place(models.Model):
    title = models.CharField(max_length=250)
    place_id = models.CharField(max_length=250)
    description_short = models.CharField(max_length=1000)
    description_long = models.TextField()

    location = PointField(blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    position = models.PositiveSmallIntegerField()
    place = models.ForeignKey("Place", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.place.title} #{self.position}"
