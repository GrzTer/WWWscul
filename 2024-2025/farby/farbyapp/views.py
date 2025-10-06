from django.shortcuts import render
from farbyapp.models import Paint


def welcome(request):
    paints = Paint.objects.all()
    return render(request, 'index.html', {'paints': paints})