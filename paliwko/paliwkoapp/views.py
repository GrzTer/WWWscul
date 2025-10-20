from django.shortcuts import render
from paliwkoapp.models import Paliwko

def welcome(request):
    paliwko = Paliwko.objects.all()
    result = None

    if request.method == 'POST':
        try:
            distance = int(request.POST.get('distance'))
            consumption = int(request.POST.get('consumption'))
            result = (distance * consumption) / 100
        except (TypeError, ValueError):
            result = None

    return render(request, 'index.html', {'paliwko': paliwko, 'result': result})
