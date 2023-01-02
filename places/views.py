from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from places.models import Place
from places.serializers import PlaceSerializer


@api_view()
def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    serializer = PlaceSerializer(place)
    return Response(serializer.data)
