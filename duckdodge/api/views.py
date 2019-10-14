from rest_framework import generics, views
from rest_framework.response import Response
import csv
from .models import Boat, Race, ImportCSV
from .serializers import BoatSerializer, RaceSerializer, ImportCSVSerializer
from .permissions import IsCreatorOrReadOnly

class RaceList(generics.ListCreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class BoatList(generics.ListCreateAPIView):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer

class RaceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsCreatorOrReadOnly, )
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class BoatDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsCreatorOrReadOnly, )
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer

class ImportCSV(views.APIView):

    def get(self, request):

        filename = './data/boats.csv'

        # Import Data
        with open(filename) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',', quotechar="'")
            for row in readCSV:
                print(row)
                # print(row[0])
                # print(row[0],row[1],row[2],)

        data = [{"status":"OK", "rows":99}]


        results = ImportCSVSerializer(data, many=True).data
        return Response(results)