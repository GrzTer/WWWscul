from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def me(request):
    start_time = datetime(2024, 9, 11, 9, 20)
    total_time = datetime.now() - start_time
    return HttpResponse("This is me working on this project for: " + str(total_time))
