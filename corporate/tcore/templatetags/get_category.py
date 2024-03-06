from django import template
from tcore.models import Kategoriler

register = template.Library()
@register.simple_tag
def get_category():
  kategoriler = Kategoriler.objects.all()
  return kategoriler