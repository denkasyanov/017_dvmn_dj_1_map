from django.urls import path

from places.views import place_detail

app_name = "places"

urlpatterns = [
    path("<int:pk>/", place_detail, name="detail"),
]
