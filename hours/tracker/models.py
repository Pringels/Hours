from django.db import models


class Hour(models.Model):
    category = models.CharField(max_length=100)
