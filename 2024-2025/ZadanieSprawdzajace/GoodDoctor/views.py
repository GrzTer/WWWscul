from django.forms.models import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from GoodDoctor.models import Wizyta, Pacjent


def num_wizyt(request):
    num_wizyt = Wizyta.objects.count()
    all_wizyty = Wizyta.objects.all()
    return render(
        request,
        "GoodDoctor/wizyta.html",
        {
            "num_wizyt": num_wizyt,
            "all_wizyty": all_wizyty,
        },
    )


def details(request, id):
    detail = get_object_or_404(Pacjent, pk=id)
    wizyty = Wizyta.objects.filter(pacjent=detail)
    return render(
        request,
        "GoodDoctor/detail.html",
        {
            "detail": detail,
            "wizyty": wizyty,
        },
    )

def pacjenci(request):
    all_pacjenci = Pacjent.objects.all()
    return render(
        request,
        "GoodDoctor/pacjenci.html",
        {
            "all_pacjenci": all_pacjenci,
        },
    )
WizytaForm = modelform_factory(Wizyta, exclude=[])
def new(request):
    if request.method == "POST":
        form = WizytaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    else:
        form = WizytaForm()
    return render(request, "GoodDoctor/new.html", {"form": form})