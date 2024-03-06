from django.urls import path
from .import views as v
urlpatterns = [
    path("", v. IndexView.as_view(), name="index"),
    path("", v.index, name="kategoriler"),
    path("technology", v. TeknolojiView.as_view(), name="technology"),
    path("sport", v. SporView.as_view(), name="sport"),
    path("healty", v. SaglikView.as_view(), name="healty"),
]