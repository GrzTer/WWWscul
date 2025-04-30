from django.shortcuts import render

from rybyapp.models import Ryby, OkresOchronny


def ryby(request):
    ryby = Ryby.objects.all()
    okres_ochronny = OkresOchronny.objects.filter(wymiar_ochronny__gt=0)
    return render(
        request, "ryby.html", {"ryby": ryby, "okres_ochronny": okres_ochronny}
    )
