from django.db import models

class FlightLog(models.Model):
    aircraft_type = models.CharField(max_length=100)
    route = models.CharField(max_length=200)
    pilot_in_command = models.CharField(max_length=100)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #..

    def __str__(self):
        return f"{self.aircraft_type} - {self.route}"
