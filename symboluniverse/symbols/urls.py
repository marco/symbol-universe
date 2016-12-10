from django.conf.urls import url
from . import views

urlpatterns = [
    # Match any number, as long as it is
    url(r'^(?P<id_string>[0-9]+)$', views.symbol, name="symbol"),
]
