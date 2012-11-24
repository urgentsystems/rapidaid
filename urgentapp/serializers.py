from django.forms import widgets
from rest_framework import serializers
from urgentapp import models

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Unit
        fields = ('id', 'position')