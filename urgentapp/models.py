from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User


# Create your models here.

class Unit(models.Model):
    unit_name = models.CharField(max_length=200)
    user = models.ForeignKey(User,null=True, blank=True)
    position = GeopositionField(default="32.82074903230932,-83.64166265624999")

    def __unicode__(self):
        return self.unit_name



class Need(models.Model):
    short_description = models.CharField(max_length=200, default="Empty")
    description = models.TextField()
    position = GeopositionField(default="32,-83")
    assigned_user = models.ForeignKey(User,null=True, blank=True)


    def __unicode__(self):
        return self.short_description



class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, default="Doe")

    class Meta:
        verbose_name_plural = "people"

    def __unicode__(self):
        return self.name

class Case(models.Model):
    assigned_unit = models.ForeignKey(Unit)


class Incident(models.Model):
    DateTime = models.DateTimeField(auto_now_add=True)
    Case = models.ForeignKey(Case)
    assigned_unit = models.ForeignKey(Unit)


class PhoneNumber(models.Model):
    area_code = models.PositiveSmallIntegerField()
    prefix = models.PositiveSmallIntegerField()
    number = models.PositiveSmallIntegerField()

class Phone_To_Person(models.Model):
    person = models.ForeignKey(Person)
    Phone = models.ForeignKey(PhoneNumber)