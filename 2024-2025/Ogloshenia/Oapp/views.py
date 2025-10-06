from django.shortcuts import render

from Oapp.models import Uzytkownik, Ogloshenia


def index(request):
    ogloshenia = Ogloshenia.objects.all()
    ogloshenia_l = Ogloshenia.objects.count()
    return render(request, 'index.html', {'ogloshenia': ogloshenia, 'ogloshenia_l': ogloshenia_l})
