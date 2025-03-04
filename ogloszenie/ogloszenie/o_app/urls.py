from django.urls import path
from .views import index, tresc, ksiazki, uzytkownik

urlpatterns = [
    path('', index, name='index'),
    path('ogloszenie/<int:pk>/', tresc, name='tresc'),
    path('uzytkownik', uzytkownik, name='uzytkownik'),
    path('ksiazki', ksiazki, name='ksiazki'),
]
