from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=2000)
    description = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True)
    pub_date = timezone.now()
    def __str__(self):
        return self.project_text