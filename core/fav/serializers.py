from rest_framework import serializers
from fav.models import FavModel

class FavSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavModel
        fields = ('id', 'car', 'food', 'star')