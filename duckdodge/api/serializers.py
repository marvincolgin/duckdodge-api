from rest_framework import serializers
from .models import Boat, Race

class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = ['id', 'boat', 'phrf', 'make' ]


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ['racedate', 'start', 'place', 'boat' ]
