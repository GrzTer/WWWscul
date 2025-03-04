from django.shortcuts import render, get_object_or_404
from .models import Ogloszenia

def index(request): 
    ogloszenia = Ogloszenia.objects.all()
    ogloszenia_l = Ogloszenia.objects.count()
    return render(request, 'index.html', {'ogloszenia': ogloszenia, 'ogloszenia_l': ogloszenia_l})

def tresc(request, pk):
    tresc = get_object_or_404(Ogloszenia, pk=pk)
    return render(request, 'tresc.html', {'tresc': tresc})

def ksiazki(request):
    ksiazka = Ogloszenia.objects.filter(kategoria=1)
    return render(request, 'ksiazki.html', {'ksiazka': ksiazka})