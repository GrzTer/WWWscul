from django.urls import path
from website import views

urlpatterns = [
    path("<int:id>", views.detail, name="detail"),

    path("room", views.room_list, name="room"),
]
# // Copyright (c) 2024 Grzegorz Tereszkiewicz all rights reserved.