from django.contrib import admin
from django.urls import include, path
from tcore.views import set_language
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tcore.urls")),
]

urlpatterns = [
    *i18n_patterns(*urlpatterns,prefix_default_language=True),
    path("set_language/<str:language>", set_language, name="set-language"),
]
