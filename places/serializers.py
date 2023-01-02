from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from places.models import Image
from places.models import Place


class PlaceFeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Place
        geo_field = "location"
        fields = ("title", "place_id", "details_url")

    details_url = serializers.SerializerMethodField()

    def get_details_url(self, place: Place):
        return place.get_absolute_url()


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            "title",
            "imgs",
            "description_short",
            "description_long",
            "coordinates",
        )

    imgs = serializers.SerializerMethodField()
    coordinates = serializers.SerializerMethodField()

    def get_imgs(self, place):
        return [
            image.image.url
            for image in Image.objects.filter(place=place).order_by("position")
        ]

    def get_coordinates(self, place: Place):
        return {
            "lat": place.location.y,
            "lng": place.location.x,
        }
