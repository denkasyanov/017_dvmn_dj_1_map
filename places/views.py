from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from places.models import Place


@api_view
def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return HttpResponse(place.title)
