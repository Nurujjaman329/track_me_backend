from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=True, blank=True)  # single date
    time = models.TimeField(null=True, blank=True)
    priority = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title
