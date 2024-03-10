from django.db import models

# Create your models here.
from django.db import models
from math import log

class Airplane(models.Model):
    airplane_id = models.IntegerField(unique=True)
    passengers = models.IntegerField(default=0)

    def __str__(self):
        return f"Airplane {self.airplane_id} with {self.passengers} passengers"

    @property
    def fuel_tank_capacity(self):
        """Calculate fuel tank capacity based on airplane ID."""
        return 200 * self.airplane_id

    @property
    def fuel_consumption_per_minute(self):
        """Calculate base fuel consumption per minute, not accounting for passengers."""
        return log(self.airplane_id) * 0.80
