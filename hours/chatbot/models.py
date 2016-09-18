from __future__ import unicode_literals

import os
from django.db import models


def get_image_path(instance, filename):
    return os.path.join('chatbot', str(instance.id), filename)

class Settings(models.Model):
    active_queue = models.ForeignKey('ResponseQueue', blank=True)
    active_bot = models.ForeignKey('Bot', blank=True)

    def __str__(self):
        return "Active Bot"

class Bot(models.Model):
    title = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.title

class ResponseQueue(models.Model):
    title = models.CharField(max_length=255, default='Default')
    response = models.ManyToManyField('Response', blank=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    content = models.CharField(max_length=255)
    partial_match = models.BooleanField(default=False)
    result = models.ForeignKey("Response")

    def __str__(self):
        return self.content


class Response(models.Model):
    content = models.CharField(max_length=1024)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    links = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return self.content

