from collections.abc import Iterable
from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Kategoriler(models.Model):
  page = models.CharField(max_length=255, verbose_name=_("Sayfa"))
  slug=models.SlugField(max_length=255,blank=True,editable=False,unique=True ,verbose_name=_("slug"))

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.page)
    super(Kategoriler,self). save(*args, **kwargs)
  def __str__(self):
    return self.page


class Postlar(models.Model):
  page = models.ForeignKey(Kategoriler, on_delete=models.CASCADE)
  title = models.CharField(max_length=255, verbose_name=_("Başlık"))
  contents = HTMLField(verbose_name=_("İçerik"))
  image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name=_("Fotoğraf"))
  release_date= models.DateTimeField(auto_now_add=True, verbose_name=_("Yayınlanma Tarihi"))

  def __str__(self):
        return f"{self.page}"
  



class Setting(models.Model):
  logo=models.ImageField(upload_to='images/', null=True,blank=True )
  title=models.CharField(max_length=255)
  keywords=models.CharField(max_length=255)
  description=models.CharField(max_length=255)
  phone_fixed=models.CharField(max_length=15)
  phone_mobile=models.CharField(max_length=15)
  email=models.EmailField()
  address=models.TextField()
  facebook_url=models.URLField(max_length=250)
  instagram_url=models.URLField(max_length=250)
  linkedin_url=models.URLField(max_length=250)
  twitter_url=models.URLField(max_length=250)
  youtube_url=models.URLField(max_length=250)



