"""shorter urls"""

from django.urls import path
from shorter.views import ShorterListView, ShorterCreateView, redirect_to_url

app_name = "shorter" # pylint: disable=invalid-name

urlpatterns = [
    path("user/<username>/", ShorterListView.as_view(), name="list"),
    path("url/create/", ShorterCreateView.as_view(), name="create"),
    path("<username>/<short_url>/", redirect_to_url, name="redirect")
]
