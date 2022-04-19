from rest_framework import serializers
from secret.models import SecretModel

class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretModel
        fields = ('id', 'secret')
        read_only_fields = ('id', )
