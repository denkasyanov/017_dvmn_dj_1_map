from adminsortable2.admin import SortableTabularInline, SortableAdminBase
from django import forms
from django.contrib import admin
from django.contrib.gis.geos import Point
from django.utils.safestring import mark_safe

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
        cleaned_place = super().clean()
        if "latitude" in self.changed_data or "longitude" in self.changed_data:
            lat, lng = cleaned_place.pop("latitude", None), cleaned_place.pop(
                "longitude", None
            )
            cleaned_place["location"] = Point(lng, lat, srid=4326)

        if not (cleaned_place.get("location") or cleaned_place.get("latitude")):
            raise forms.ValidationError({"location": "Location is required"})
        return cleaned_place


class ImageInline(SortableTabularInline):
    model = Image
    fields = ("image", "preview", "position")
    readonly_fields = ("preview",)

    def preview(self, image):
        url = image.image.url
        height = min(image.image.height, 200)
        return mark_safe(f"<img src='{url}' height='{height}' />")


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    form = PlaceForm
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
