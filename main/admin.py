from django.contrib import admin
from .models import Tutorials

class TutorialAdmin(admin.ModelAdmin):

    fieldsets =[("(title/date)",{ "fields":["title","published"]}),
                ("content", { "fields":["content"]})]

admin.site.register(Tutorials, TutorialAdmin)
