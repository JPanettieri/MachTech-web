from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField(default=timezone.now)
    def __str__(self):
        return self.name