from django.forms import modelform_factory
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from website.models import Meeting, Room

MeetingForm=modelform_factory(Meeting,exclude=[])
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
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "website/detail.html", {"meeting": meeting})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def me(request):
    start_time = datetime(2024, 9, 11, 9, 20)
    total_time = datetime.now() - start_time
    return HttpResponse("This is me working on this project for: " + str(total_time))

def room_list(request):
    room = Room.objects.all()
    return render(request, "website/room_list.html", {"room": room})

def new(request):
    form=MeetingForm()
    if request.method=="POST":
        form=MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("website:welcome")
    else:
        form=MeetingForm()
    return render(request, "website/new.html", {"form":form})






































# // Copyright (c) 2024 Grzegorz Tereszkiewicz all rights reserved.