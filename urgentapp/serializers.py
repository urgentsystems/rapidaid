from django.forms import widgets
from rest_framework import serializers
from urgentapp import models
from django.contrib.auth.models import User

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Unit
        fields = ('id','unit_name', 'position')




class UserSerializer(serializers.ModelSerializer):
    unit = serializers.ManyPrimaryKeyRelatedField()

    class Meta:
        model = User
        fields = ('id', 'username', 'unit')