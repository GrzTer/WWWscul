from django.shortcuts import render, redirect

from beautyapp.models import Uslugi, Kadra


def welcome(request):
    uslugi = Uslugi.objects.all()
    return render(request, 'beauty.html', {"uslugi": uslugi})


def kadra(request):
    kadry = Kadra.objects.all()
    return render(request, 'kadra.html', {"kadry": kadry})


def new(request):
    if request.method == 'POST':
        imie = request.POST.get('imie')
        nazwisko = request.POST.get('nazwisko')
        stanowisko = request.POST.get('stanowisko')
        Kadra.objects.create(imie=imie, nazwisko=nazwisko, stanowisko=stanowisko)
        return redirect('kadra')

    return render(request, 'new.html')