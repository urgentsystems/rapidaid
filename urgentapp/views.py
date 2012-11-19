# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    t = loader.get_template('index.html')
    return HttpResponse(t.render())