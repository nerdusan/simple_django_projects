from django.shortcuts import render
from django.views import View
from bincom.models import AnnouncedPuResults

# Create your views here.
def index(request):
    ctx = {'ranger': list(range(8, 28))}
    return render(request, 'bincom/index.html', ctx)

class PuView(View):
    def get(self, request, pu_id):
        results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=pu_id).values()
        x = {"results":results, "pu_id":pu_id, }
        return render(request, 'bincom/pu.html', x)
