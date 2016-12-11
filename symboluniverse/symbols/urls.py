from django.conf.urls import url
from . import views

urlpatterns = [
    # Match either HTML number codes or Unicode hexadecimal codes
    url(r'^h/(?P<html_number_string>[0-9]+)$', views.symbol, name='symbol'),
    url(r'^u/(?P<unicode_hexadecimal_string>[0-9a-fA-F]+)$', views.symbol,
        name='symbol'),
]
