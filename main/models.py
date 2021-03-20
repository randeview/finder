from datetime import datetime
from django.contrib.gis.db import models
from django.contrib.gis.measure import D
from django.contrib.gis.geos import *


class Event(models.Model):
    location = models.PointField(null=True, blank=True)
    title = models.CharField("Названиае события", max_length=400, null=True, blank=True)
    link = models.URLField("Ссылка на событие", null=True, blank=True)
    createdAt = models.BigIntegerField('Дата создания', null=True, blank=True)
    left = models.IntegerField()
    tags = models.CharField("Тэги", max_length=1000, blank=True, null=True)
    def __str__(self):
        return self.title

    @property
    def created_at(self):
        return datetime.fromtimestamp(self.createdAt / 1000.0)

    @staticmethod
    def get_near(lat: float, long: float):
        return

    class Meta:
        verbose_name = 'События'
        verbose_name_plural = 'Событии'
