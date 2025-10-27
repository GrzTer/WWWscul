from django.shortcuts import render, redirect

from komisapp.models import Zamowienia, Samochody


def zamowienia(request):
    zamowienias = Zamowienia.objects.all()
    return render(request, 'zamowienia.html', {'zamowienia': zamowienias})

def auta(request):
    samochody = Samochody.objects.all()
    return render(request, 'auta.html', {'samochody': samochody})

def new(request):
    if request.method == 'POST':
        marka = request.POST.get('marka')
        model = request.POST.get('model')
        rocznik = request.POST.get('rocznik')
        kolor = request.POST.get('kolor')
        stan = request.POST.get('stan')
        Samochody.objects.create(marka=marka, model=model, rocznik=rocznik, kolor=kolor, stan=stan)
        return redirect('auta')
    return render(request, 'new.html')