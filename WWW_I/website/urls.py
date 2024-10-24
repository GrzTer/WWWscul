from django.urls import path
from website import views

urlpatterns = [
    path("<int:id>", views.detail, name="detail"),

    path("room", views.room_list, name="room"),
]