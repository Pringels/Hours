from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    post_date = models.DateField()
    content = models.TextField()
    slug = models.CharField(max_length=256)

    class Meta:
        get_latest_by = "post_date"
