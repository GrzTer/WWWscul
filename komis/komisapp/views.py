from django.forms.models import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404
from komisapp.models import Zamowienia, Samochody

SamochodyForm = modelform_factory(Samochody, exclude=[])


def zamowienia(request):
    zamowienias = Zamowienia.objects.all()
    return render(request, 'zamowienia.html', {'zamowienia': zamowienias})


def auta(request):
    samochody = Samochody.objects.all()
    return render(request, 'auta.html', {'samochody': samochody})


def new(request):
    if request.method == 'POST':
        form = SamochodyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auta')
    else:
        form = SamochodyForm()

    return render(request, 'new.html', {'form': form})


def edytuj(request, id):
    samochod = get_object_or_404(Samochody, id=id)
    if request.method == 'POST':
        form = SamochodyForm(request.POST, instance=samochod)
        if form.is_valid():
            form.save()
            return redirect('auta')
    else:
        form = SamochodyForm(instance=samochod)

    return render(request, 'new.html', {'form': form})


def kasuj(request, id):
    samochody = get_object_or_404(Samochody, id=id)
    if request.method == 'POST':
        samochody.delete()
        return redirect('auta')