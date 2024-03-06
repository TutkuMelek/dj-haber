from django.contrib import admin
from django.http.request import HttpRequest
from .models import Kategoriler ,Postlar, Setting
from modeltranslation.admin import TranslationAdmin
from .admin_mixins import CommonMedia


class BaseAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Kategoriler)
class KategorilerAdmin(TranslationAdmin, CommonMedia):
    list_display = ('page',)


@admin.register(Postlar)
class PostlarAdmin(TranslationAdmin, CommonMedia):
    list_display = ('page', 'title', 'contents', 'release_date')


@admin.register(Setting)
class SettingAdmin(TranslationAdmin, CommonMedia,BaseAdmin):
    list_display = ('title',)


