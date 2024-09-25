from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from website.models import Meeting


def welcome(request):
    num_meetings = Meeting.objects.count()
    meeting = Meeting.objects.all()
    return render(
        request,
        "website/welcome.html",
        {
            "num_meetings": num_meetings,
            "message": "Witaj na stronie spotkań!",
            "meeting": meeting,
        },
    )

def detail(request, id):
    meeting=get_object_or_404(Meeting,pk=id)
    return render(request, "website/detail.html",{"meeting": meeting})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def me(request):
    start_time = datetime(2024, 9, 11, 9, 20)
    total_time = datetime.now() - start_time
    return HttpResponse("This is me working on this project for: " + str(total_time))
