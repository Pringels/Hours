from django.contrib import admin

from chatbot.models import Message
from chatbot.models import Response
from chatbot.models import ResponseQueue
from chatbot.models import Settings

admin.site.register(Message)
admin.site.register(Response)
admin.site.register(ResponseQueue)
admin.site.register(Settings)
