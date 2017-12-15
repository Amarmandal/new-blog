from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    text = models.TextField()
    create_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    def published(self):
        self.published_date = timezone.now()
        self.short = self.text[0:250]
        self.save()

    def __str__(self):
        return self.title

