from django.shortcuts import render
from .models import Ogloszenia

def index(request): 
    ogloszenia = Ogloszenia.objects.all()
    return render(request, 'index.html', {'ogloszenia': ogloszenia})

