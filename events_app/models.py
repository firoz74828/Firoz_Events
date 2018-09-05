from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    event_header= models.CharField(max_length=300)
    event_content = models.CharField(max_length=600)
    event_image = models.ImageField(upload_to='', blank=True, null=True)
    event_address = models.CharField(max_length=300)
    event_date = models.DateTimeField()


    def __str__(self):
        return self.event_header