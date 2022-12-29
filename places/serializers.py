from django.templatetags.static import static
from rest_framework.serializers import SerializerMethodField
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from places.models import Place


class PlaceFeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Place
        geo_field = "location"
        fields = ("title", "place_id", "details_url")

    details_url = SerializerMethodField()

    def get_details_url(self, place: Place):
        return static(f"places/{place.place_id}.json")
