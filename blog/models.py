from django.db import models
from django.utils import timezone

# Create your models here.


class MyPost(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 250)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    def publish_post(self):
        self.date_published = timezone.now()
        self.save()

    def __str__(self):
        return self.title
