from django.db import models
from Traveler.models import Traveler

class Trip(models.Model):
    destination = models.CharField(
        max_length=100,
        help_text="*Destination name."
    )
    summary = models.TextField()
    start_date = models.DateField()
    duration = models.PositiveSmallIntegerField(
        default=1,
        help_text="*Duration in days is expected."
    )
    image_url = models.URLField(
        blank=True,
        null=True
    )
    traveler = models.ForeignKey(
        Traveler,
        on_delete=models.CASCADE,
        related_name="trips"
    )

    def __str__(self):
        return self.destination
