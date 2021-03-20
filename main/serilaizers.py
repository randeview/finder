from datetime import datetime

from rest_framework import serializers

from .models import Event
from django.contrib.gis.geos import Point


class EventBaseSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        point = Point(validated_data.pop('long'), validated_data.pop('lat'))
        validated_data['location'] = point
        return super(EventBaseSerializer, self).create(validated_data)

    class Meta:
        model = Event
        fields = ['id', 'title', 'link', 'createdAt', 'left', 'tags']


class EventListSerializer(EventBaseSerializer):
    long = serializers.FloatField(source='location.x')
    lat = serializers.FloatField(source='location.y')

    class Meta:
        model = Event
        fields = EventBaseSerializer.Meta.fields + ['long', 'lat']


class EventCreateSerializer(EventBaseSerializer):
    long = serializers.FloatField()
    lat = serializers.FloatField()

    class Meta:
        model = Event
        fields = EventBaseSerializer.Meta.fields + ['long', 'lat']


class EventGetSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    long = serializers.FloatField()
    radius = serializers.IntegerField()
    tags = serializers.CharField(max_length=500)
