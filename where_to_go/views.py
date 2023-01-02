import json

from django.shortcuts import render
from djangorestframework_camel_case.util import camelize

from places.models import Place
from places.serializers import PlaceFeatureSerializer


def main_page(request):
    places = Place.objects.all()

    map_features = PlaceFeatureSerializer(places, many=True).data

    # Please the front-end
    map_features = camelize(map_features)

    # Temporary hack to get rid of non-primitive structures
    map_features = json.loads(json.dumps(map_features))

    return render(request, "index.html", context={"map_features": map_features})
