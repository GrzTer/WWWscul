from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("details/<int:id>", views.details, name="details"),
    path("pacjenci/", views.pacjenci, name="pacjenci"),
]