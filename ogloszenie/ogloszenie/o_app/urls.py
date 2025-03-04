from django.urls import path
from .views import index, tresc, ksiazki

urlpatterns = [
    path('', index, name='index'),
    path('ogloszenie/<int:pk>/', tresc, name='tresc'),
    path('ksiazki', ksiazki, name='ksiazki'),
]
