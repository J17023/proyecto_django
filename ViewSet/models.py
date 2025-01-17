from django.db import models
from datetime import datetime,timezone

# Create your models here.

class programmer_model(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    creation_date = models.DateField(default=datetime.now(timezone.utc))