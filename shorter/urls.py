"""shorter urls"""

from django.urls import path
from django.contrib.auth.views import LogoutView

from shorter.views import (
    LandingView,
    ShorterLoginView,
    ShorterListView,
    ShorterCreateView,
    redirect_to_url,
)

app_name = "shorter" # pylint: disable=invalid-name

urlpatterns = [
    path("", LandingView.as_view(), name="landing"),
    path("login/", ShorterLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="shorter:landing"), name="logout"),
    path("user/<username>/", ShorterListView.as_view(), name="list"),
    path("url/create/", ShorterCreateView.as_view(), name="create"),
    path("<username>/<short_url>/", redirect_to_url, name="redirect"),
]
