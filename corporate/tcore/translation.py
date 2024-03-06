from modeltranslation.translator import register,TranslationOptions
from .models import Kategoriler,Postlar,Setting


@register(Kategoriler)
class KategorilerTranslationOptions(TranslationOptions):
  fields = ('page',)
 

@register(Postlar)
class PostlarTranslationOptions(TranslationOptions):
  fields = ('page', 'title', 'contents', 'release_date')
 

@register(Setting)
class SettingTranslationOptions(TranslationOptions):
  fields = ('title', 'keywords','description',)
 