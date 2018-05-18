from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^delete/(?P<course_id>\d+)$', views.show_or_destroy)
]
