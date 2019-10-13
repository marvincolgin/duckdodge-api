from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Boat(models.Model):
    id = models.AutoField(primary_key=True)
    boat = models.CharField(max_length=255)
    phrf = models.IntegerField(default=None, null=True)
    make = models.CharField(max_length=50, default=None, null=True)

    def __str__(self):
        return f'{self.boat} / {self.make} phrf:{self.phrf}'

class Race(models.Model):
    racedate = models.DateField()
    start = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    place = models.PositiveIntegerField()
    boat = models.CharField(max_length=255)

    class Meta:
        unique_together = ('racedate', 'start', 'place')

    def __str__(self):
        return f'{self.racedate} Start:{self.start} Place:{self.place} {self.boat}'
