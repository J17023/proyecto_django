from django.db import models

class Tutorials(models.Model):
    title = models.CharField(max_length= 50)
    content = models.TextField()
    published = models.DateTimeField()

    def __str__(self):
        return self.tutorial_title
