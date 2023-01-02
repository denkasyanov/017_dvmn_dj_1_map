import requests
from django.contrib.gis.geos import Point
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from places.models import Image
from places.models import Place


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

        place, _ = Place.objects.get_or_create(
            title=imported_place["title"],
            defaults={
                "description_short": imported_place["description_short"],
                "description_long": imported_place["description_long"],
                "location": Point(
                    x=float(imported_place["coordinates"]["lng"]),
                    y=float(imported_place["coordinates"]["lat"]),
                ),
            },
        )

        # Assuming:
        #  1) We are creating images for a new place (no prior images)
        #  2) Images are in correct order
        image_position = 1

        for img_url in imported_place["imgs"]:

            response = requests.get(img_url)

            if not response.ok:
                raise CommandError(f"Couldn't download {img_url}")

            img_name = img_url.split("/")[-1]

            Image.objects.create(
                image=ContentFile(response.content, name=img_name),
                position=image_position,
                place=place,
            )

            image_position += 1
