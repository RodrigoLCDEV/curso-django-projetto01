# https://docs.djangoproject.com/pt-br/3.2/topics/http/urls/
from django.urls import path

from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/<int:id>/", views.recipe, name="detail"),
]
