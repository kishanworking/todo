from django.db import models
from django.utils import timezone
# Create your models here.

class Attendencedata(models.Model):

    total_break = models.CharField(max_length=100)
    total_working_hours = models.CharField(max_length=100)
    total_break = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    
    end = models.DateTimeField(auto_now=True)
    start = models.DateTimeField(auto_now=True)
    now_date = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.date
    

