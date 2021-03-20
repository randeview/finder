from django.contrib.gis.geos import Point
from django.db.models import Q
from rest_framework import mixins, status
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from math import sin, cos, sqrt, atan2, radians
from .models import Event
from .serilaizers import EventListSerializer, EventCreateSerializer, EventGetSerializer
from django.contrib.gis.measure import Distance


class EventCreateView(GenericAPIView):
    serializer_class = EventCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={'message': 'ok'}, status=status.HTTP_201_CREATED)


class EventsGetView(mixins.ListModelMixin, GenericAPIView):
    serializer_class = EventGetSerializer
    queryset = Event.objects.all()

    def get_queryset(self, **kwargs):
        return super(EventsGetView, self).get_queryset()

    def post(self, request, *args, **kwargs):
        serializer_data = self.get_serializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        point = Point(serializer_data.data.get('long'), serializer_data.data.get('lat'))
        radius = serializer_data.data.get('radius')
        tags = serializer_data.data.get('tags')
        query = self.queryset.filter((Q(location__distance_lt=(point, Distance(km=radius))) | Q(tags__icontains=tags)))
        sorted_query = sorted(query, key=lambda t: t.created_at)
        serializer = EventListSerializer(instance=sorted_query, many=True)
        data = {
            'count': query.count(),
            'data': serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)
