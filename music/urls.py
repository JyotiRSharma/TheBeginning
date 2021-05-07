from django.urls import re_path, path
from . import views

urlpatterns = [
    # /music/
    re_path(r'^$', views.index, name='index'),

    # /music/71
    re_path(r'^(?P<album_id>[0-9]+)$', views.details, name='details'),
]