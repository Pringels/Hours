import json, os

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from hours.settings import STATIC_URL

from chatbot.models import Message, Response, ResponseQueue, Settings

def home(request):
    context = {}
    app_settings = Settings.objects.all().first()
    response = app_settings.active_queue.response.all()[0]
    context = build_context(context, response)
    context["bot_name"] = app_settings.active_bot.title
    context["bot_profile_pic"] = app_settings.active_bot.profile_pic.url
    return render(request, 'chatbot/home.html', context)

@csrf_exempt
def get_response(request):
    request_string = request.POST.get("message", "")
    counter = request.POST.get("counter", 0)
    message = Message.objects.filter(content__contains=request_string).first()

    context = {}

    if (message == None) or (message.partial_match is False and message.content != request_string):
        app_settings = Settings.objects.all().first()
        try:
            response = app_settings.active_queue.response.all()[int(counter)]
            context['increment'] = True
        except ObjectDoesNotExist:
            response = app_settings.active_queue.response.all()[0]
            context['reset'] = True
        except IndexError:
            response = app_settings.active_queue.response.all()[0]
            context['reset'] = True

    else:
        response = message.result

    context = json.dumps(build_context(context, response))

    return HttpResponse(context)


def build_context(context, response):
    context['message'] = response.content
    context['image'] = False
    context['links'] = []

    if response.image:
        context['image'] = os.path.join(STATIC_URL, 'images', response.image.url)

    if response.links:
        for link in response.links.all():
            context['links'].append(link.content)

    return context
