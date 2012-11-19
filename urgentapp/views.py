# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from urgentapp.models import Unit

@login_required
def index(request):
    unit_list = Unit.objects.all()
    t = loader.get_template('index.html')
    c = Context({
        'unit_list' : unit_list,
    })
    return HttpResponse(t.render(c))