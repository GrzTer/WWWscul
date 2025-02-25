from django.shortcuts import render
from .models import Ogloszenia

def index(request): 
    ogloszenia = Ogloszenia.objects.all()
    ogloszenia_l = Ogloszenia.objects.count()
    return render(request, 'index.html', {'ogloszenia': ogloszenia, 'ogloszenia_l': ogloszenia_l})