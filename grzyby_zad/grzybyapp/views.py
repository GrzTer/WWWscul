from django.shortcuts import render

from grzybyapp.models import Grzyby


def grzyby_list(request):
    grzyby = Grzyby.objects.all()
    return render(request, 'index.html', {'grzyby': grzyby})