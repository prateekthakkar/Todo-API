from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=500)
    completed = models.BooleanField(null=True, blank=True, default=None)
    url = models.CharField(max_length=500, null=True, blank=True, default=None)
    order = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title
    