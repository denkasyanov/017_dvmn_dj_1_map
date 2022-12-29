from django.urls import path

from places.views import place_detail


urlpatterns = [
    path("<int:pk>/", place_detail, name="place_detail"),
]
