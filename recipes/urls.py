# https://docs.djangoproject.com/pt-br/3.2/topics/http/urls/
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("recipes/<int:id>/", views.recipe),
]
