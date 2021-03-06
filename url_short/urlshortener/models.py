from django.db import models
from .utils import create_shortened_url
from django.contrib.auth.models import User

class Shortener(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["short_url"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}' 

    
    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_shortened_url(self)
        super().save(*args, **kwargs)