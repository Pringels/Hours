import os

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.conf import settings

key = 'MLiwwrk0nLu3i2AWCtMKWkanV8T9u56H'

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

# Create your views here.

@csrf_exempt
def upload(request):
    post = request.POST.get('test');
    auth_key = request.POST.get('auth_key');

    if auth_key:
        if auth_key != key:
            return HttpResponse("Invalid auth key")
    else:
        return HttpResponse("Missing auth key")

    handle_uploaded_file(request.FILES['test'])

    return HttpResponse("success")

def handle_uploaded_file(f):

    img_path = os.path.join(settings.MEDIA_ROOT, 'test_image.jpg')
    print img_path
    with open(img_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
