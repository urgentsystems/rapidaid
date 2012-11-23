"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from urgentapp.models import Unit


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)



class UrgentTestCasse(TestCase):
    def setUp(self):
        self.kerry = Unit.objects.create(unit_name="kerry")

    def test_get_unit_name(self):
        self.assertEqual(self.kerry.unit_name, 'kerry')