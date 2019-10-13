from rest_framework import generics
from .models import Boat, Race
from .serializers import BoatSerializer, RaceSerializer
# from .permissions import IsCreatorOrReadOnly

class RaceList(generics.ListCreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class BoatList(generics.ListCreateAPIView):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer

class RaceDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsCreatorOrReadOnly, )
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class BoatDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsCreatorOrReadOnly, )
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer
