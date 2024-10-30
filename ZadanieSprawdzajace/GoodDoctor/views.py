from django.shortcuts import render, get_object_or_404
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
    details = get_object_or_404(Pacjent, pk=id)
    return render(
        request,
        "GoodDoctor/detail.html",
        {
            "details": details,
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