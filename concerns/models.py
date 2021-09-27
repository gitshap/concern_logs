from django.db import models


class Concerns(models.Model):
    person = models.CharField(max_length=255, blank=True)
    findings = models.CharField(max_length=255, blank=True)
    resolution = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.person}'s problem is {self.status}"
