import datetime
from django.test import TestCase
from .models import Boat, Race


class BoatTest(TestCase):

    def setUp(self):
        Boat.objects.create(
            boat='Fat Chance', phrf=186, make='J/24'
        )

    def test_boat(self):
        boat = Boat.objects.get(boat='Fat Chance')
        self.assertEqual(boat.phrf, 186)


class RaceTest(TestCase):

    def setUp(self):
        Race.objects.create(
            racedate=datetime.datetime(2007, 1, 1),
            start=2,
            place=3,
            boat='Fat Chance'
        )

    def test_race(self):
        race = Race.objects.get(
            racedate=datetime.datetime(2007, 1, 1),
            start=2,
            place=3
        )
        self.assertEqual(race.boat, 'Fat Chance')
