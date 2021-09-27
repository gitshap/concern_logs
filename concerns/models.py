from django.db import models

class Concerns(models.Model):
    person = models.CharField(max_length=255)
    findings = models.CharField(max_length=255)
    resolution = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.person}'s problem is {self.status}"


