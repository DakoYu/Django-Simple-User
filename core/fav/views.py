from rest_framework import viewsets
from rest_framework.response import Response
from fav.serializers import FavSerializer
from fav.models import FavModel

class FavView(viewsets.ViewSet):
    queryset = FavModel.objects.all()
    serializer_class = FavSerializer

    def list(self, request):
        queryset = FavModel.objects.all()
        serializer = FavSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = FavSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)