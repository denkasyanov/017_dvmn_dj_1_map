import requests
from django.contrib.gis.geos import Point
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from places.models import Image
from places.models import Place


def load_image(place, img_url, position):
    response = requests.get(img_url)

    if not response.ok:
        raise CommandError(f"Couldn't download {img_url}")

    img_name = img_url.split("/")[-1]

    Image.objects.create(
        image=ContentFile(response.content, name=img_name),
        position=position,
        place=place,
    )


class Command(BaseCommand):
    help = "Loads Place with its images to the website"

    def add_arguments(self, parser):
        parser.add_argument("place_url", type=str)

    def handle(self, *args, **options):
        place_url = options.get("place_url")
        response = requests.get(place_url)

        if not response.ok:
            raise CommandError(f"Couldn't download {place_url}")

        imported_place = response.json()

        coordinates = imported_place.get("coordinates", {"lng": "0.0", "lat": "0.0"})

        place, _ = Place.objects.get_or_create(
            title=imported_place["title"],
            defaults={
                "description_short": imported_place.get("description_short", ""),
                "description_long": imported_place.get("description_long", ""),
                "location": Point(
                    x=float(coordinates["lng"]),
                    y=float(coordinates["lat"]),
                ),
            },
        )

        # Assumptions:
        #  1) We are creating images for a new place (no prior images)
        #  2) Images are in correct order
        for image_position, img_url in enumerate(imported_place["imgs"]):
            load_image(place, img_url, image_position + 1)
