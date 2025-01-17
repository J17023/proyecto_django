from django.db import models
from datetime import datetime,timezone,timedelta

def remove_date_offset():
    hour_offset = timedelta(hours=5)
    current_hour = datetime.now(timezone.utc)- hour_offset
    return current_hour.date()

# Create your models here.

class Programmer_model(models.Model):
    name = models.CharField(max_length=40)
    position = models.CharField(max_length=30)
    hire_date = models.DateField(default= remove_date_offset)

