from django import forms
from django.contrib import admin
from django.contrib.gis.geos import Point

from places.models import Image
from places.models import Place


class PlaceForm(forms.ModelForm):
    """
    This form can be used by any model that has "coordinates" field.
    It will show a better looking map than the default one
    """

    latitude = forms.FloatField(required=False)
    longitude = forms.FloatField(required=False)

    class Meta:
        model = Place
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        location = self.initial.get("location", None)
        if isinstance(location, Point):
            self.initial["longitude"], self.initial["latitude"] = location.tuple

    def clean(self):
        data = super().clean()
        if "latitude" in self.changed_data or "longitude" in self.changed_data:
            lat, lng = data.pop("latitude", None), data.pop("longitude", None)
            data["location"] = Point(lng, lat, srid=4326)

        if not (data.get("location") or data.get("latitude")):
            raise forms.ValidationError({"location": "Location is required"})
        return data


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    form = PlaceForm
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
