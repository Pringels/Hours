from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    post_date = models.DateTimeField()
    content = models.TextField()
    slug = models.CharField(max_length=256)

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = "post_date"

class Comment(models.Model):
    author = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.author

    class Meta:
        ordering = ('-pub_date',)
