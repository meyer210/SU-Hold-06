from django.contrib import admin
from .models import Project

# Register your models here.
class Project(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields' : ['title']}),
    ]
admin.site.register(Project)