from django.shortcuts import render
from django.http import HttpResponse

from tracker.models import Hour;


def index(request):
    context = {}
    context["test"] = "testing"

    context["study"] = Hour.objects.filter(category="study").count() % 3
    context["game"] = range(Hour.objects.filter(category="game").count())
    context["exercise"] = Hour.objects.filter(category="exercise").count() % 4

    return render(request, 'tracker/index.html', context)

def get_hours(request):
    output = "sample output"
    return HttpResponse(output)

def redeem_hour(request):
    category = request.POST["type"]
    hour = Hour()
    hour.category = category
    hour.save()

    output = "Earned" + category + "Hour"
    return HttpResponse(output)

def spend_hours(request):

    hour = Hour()
    hour.category = "game"
    hour.save()

    output = "Gaming hour claimed!"
    return HttpResponse(output)

def spend_game_hour(request):
    Hour.objects.filter(category="game").first().delete()
    output = "Gaming hour spent"
    return HttpResponse(output)
