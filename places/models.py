from django.contrib.gis.db.models import PointField
from django.db import models
from django.templatetags.static import static
from django.urls import reverse


class Place(models.Model):
    title = models.CharField(max_length=250)
    place_id = models.CharField(max_length=250)
    description_short = models.CharField(max_length=1000)
    description_long = models.TextField()

    location = PointField(blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("places:detail", args=(self.id,))


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    position = models.PositiveSmallIntegerField(
        default=0, blank=False, null=False, db_index=True
    )
    place = models.ForeignKey("Place", on_delete=models.CASCADE)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f"{self.place.title} #{self.position}"
