import json
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from bonsai.models import BonsaiStatus

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login

auth_key = "PCd11GjTN1aBRk1HBYb2iG91Ym5Mx94o"

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('bonsai:home'))
    context = {"failed": True}
    return render(request, 'bonsai/login.html', context)

def home(request):
    if request.user.is_authenticated():
        context = {}
        latest_moisture_reading = BonsaiStatus.objects.latest("post_date")
        context["latest_moisture_reading"] = int(((4096.00 - int(latest_moisture_reading.moisture)) / 4096) * 100)
        return render(request, 'bonsai/home.html', context)
    else:
        return render(request, 'bonsai/login.html')


@csrf_exempt
def update(request):
    moisture_reading = request.POST.get("data", "")
    key = request.POST.get("key", "")

    if key == auth_key:
        status = BonsaiStatus()
        status.moisture = moisture_reading
        status.save()
        return HttpResponse("success")

    return HttpResponse("auth failed")

def fetch(request):
    latest_moisture_reading = int(BonsaiStatus.objects.latest("post_date").moisture)
    return HttpResponse(latest_moisture_reading)

def fetch_more(request):
    latest_moisture_readings = BonsaiStatus.objects.order_by('-post_date')[:10]
    json_out = []
    for item in latest_moisture_readings:
        json_out.append(item.moisture)
    latest_reading = latest_moisture_readings.first().post_date.replace(tzinfo=None)
    timedelta = datetime.datetime.now() - latest_reading
    latest_reading = latest_reading.replace(second=0, microsecond=0)
    json_out = {
        "data": json_out,
        "date": str(latest_reading).encode('utf-8'),
        "delta": timedelta.days,
    }

    json_out = json.dumps(json_out)
    return HttpResponse(json_out)
