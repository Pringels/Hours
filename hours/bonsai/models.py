from django.db import models


class BonsaiStatus(models.Model):
    moisture = models.CharField(max_length=5)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.moisture
