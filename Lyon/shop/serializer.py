from rest_framework import serializers
from .models import Basic


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basic
        fields = (
            'id',
            'name',
            'lat',
            'lng'
        )
