from django.db import models
from django.utils import timezone

my_local_time = timezone.localtime(timezone.now())


class Concerns(models.Model):
    # case id
    person = models.CharField(max_length=255, blank=True)
    problem = models.CharField(max_length=255, blank=True)
    resolution = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=timezone.now)
    updated_at = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return f"{self.person}'s problem is {self.status}"
