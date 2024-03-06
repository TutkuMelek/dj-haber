from urllib.parse import urlparse
from django.shortcuts import render
from django.urls.exceptions import Resolver404 
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve,reverse
from django.views.generic import TemplateView
from django.utils import translation
from .models import Kategoriler
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None

        if view:
            translation.activate(language)
            next_url = reverse(
                view.url_name, args=view.args, kwargs=view.kwargs)
            response = HttpResponseRedirect(next_url)
        else:
            response = HttpResponseRedirect("/")

        return response


class IndexView(TemplateView):
  template_name="index.html"

class DünyaView(TemplateView):
  template_name="world.html"
  

class TeknolojiView(TemplateView):
  template_name="technology.html"

class SporView(TemplateView):
  template_name="sport.html"

class SaglikView(TemplateView):
  template_name="healty.html"


def index(request):
    pages = Kategoriler.objects.all()
    return render(request, 'base.html', context={'pages': pages})
