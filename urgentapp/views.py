# Create your views here.

from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.gis.shortcuts import render_to_kml
from rest_framework import generics
from django.contrib.auth.models import User

from urgentapp.serializers import UnitSerializer, UserSerializer
from urgentapp.models import Unit



@login_required
def index(request):
    unit_list = Unit.objects.all()
    c = RequestContext(request, {
        'unit_list' : unit_list,
        })

    return render_to_response('index.html',c)




@login_required
def get_units(request):
    unit_list = Unit.objects.all()

    return render_to_kml('xml/units.kml', {'unit_list':unit_list})




class UnitList(generics.ListCreateAPIView):
    model = Unit
    serializer_class = UnitSerializer

class UnitDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Unit
    serializer_class = UnitSerializer


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer

class UserInstance(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer