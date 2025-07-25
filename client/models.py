# client/models.py
from django.db import models
from django.utils import timezone
class Client(models.Model):
    name = models.CharField(max_length=200)
    condition = models.TextField(help_text="Describe the client's condition")
    treatment = models.TextField(help_text="Initial treatment or notes")
    date_time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    
class TreatmentSession(models.Model):
    client = models.ForeignKey(Client, related_name="sessions", on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)
    treatment_notes = models.TextField(help_text="Notes of the treatment session")
    def __str__(self):
        return f"{self.client.name} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"