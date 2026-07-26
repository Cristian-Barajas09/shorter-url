"""shorter views"""

from typing import Any

from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from shorter.models import ShortURL
from shorter.forms import ShortURLForm


class LandingView(TemplateView):
    """landing page view"""

    template_name = "shorter/landing.html"


class ShorterLoginView(LoginView):
    """custom login view"""

    template_name = "shorter/login.html"
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy("shorter:list", kwargs={"username": self.request.user.username})

class ShorterListView(ListView):
    """shorter list view"""

    template_name = "shorter/list.html"
    model = ShortURL
    queryset = ShortURL.audit.get_queryset()
    context_object_name = "short_urls"

    def get_queryset(self) -> QuerySet[Any]:
        query = super().get_queryset()\
            .filter(user__username=self.kwargs.get('username'))
        search = self.request.GET.get('search')

        if search:
            query = query.filter(name__icontains=search)

        return query

class ShorterCreateView(LoginRequiredMixin, CreateView):
    """shorter create view"""

    form_class = ShortURLForm
    template_name = "shorter/create_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return  reverse_lazy("shorter:list", kwargs={ "username": self.request.user.username })


def redirect_to_url(_: HttpRequest, username: str, short_url: str):
    """redirect to selected url"""

    url: ShortURL = get_object_or_404(ShortURL.audit, user__username=username, name=short_url)

    return HttpResponseRedirect(url.original_url)
