from django.db import models
from datetime import datetime, timezone,timedelta

def remove_timezone_offset():
    timezone_offset = timedelta (hours= 5)
    adjusted_time = datetime.now(timezone.utc) - timezone_offset
    return adjusted_time

class Tutorials(models.Model):
    title = models.CharField(max_length= 50)
    content = models.TextField()
    published = models.DateTimeField(default=remove_timezone_offset)

    def __str__(self):
        return self.tutorial_title
