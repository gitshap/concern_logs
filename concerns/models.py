from django.db import models
from django.utils import timezone

my_local_time = timezone.localtime(timezone.now())


class Concerns(models.Model):
    DONE = 'Done'
    WAITING = 'Waiting'

    STATUS_CHOICES = [
        (DONE, 'Done'),
        (WAITING, 'Waiting')
    ]

    person = models.CharField(max_length=255, blank=True)
    problem = models.CharField(max_length=255, blank=True)
    resolution = models.CharField(max_length=255, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=DONE, blank=True)
    additional_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.person}'s problem is {self.status}"


class Name(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
