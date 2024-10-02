from django.shortcuts import render
from GoodDoctor.models import Wizyta, Pacjent


def num_wizyt(request):
    num_wizyt = Wizyta.objects.count()
    all_pacjenci = Pacjent.objects.all()
    return render(
        request,
        "GoodDoctor/wizyta.html",
        {
            "num_wizyt": num_wizyt,
            "all_pacjenci": all_pacjenci,
        },
    )
