from django.db import models
from core.models import TimeStampedModel


class Equipment(TimeStampedModel):
    label = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.label} - {self.name} is in {self.location}'
